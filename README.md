```python
python -m unittest test_my_math.py

```

```python
pytest
```

```python
pytest -v test_reqres_api.py
```

Good one ⚡️ Running tests in parallel can make your test suite **much faster**. With **pytest**, you do this using the [`pytest-xdist`](https://pypi.org/project/pytest-xdist/) plugin.

---

## 🛠️ Setup

Install the plugin:

```bash
pip install pytest-xdist
```

---

## ▶️ Run all tests in parallel

### 1. Run with N processes (e.g., 4)

```bash
pytest -n 4
```

This will split tests across **4 workers**.

---

### 2. Run on all available CPU cores

```bash
pytest -n auto
```

Pytest will auto-detect the number of CPU cores and distribute tests across them.

---

### 3. Run with load balancing

```bash
pytest -n auto --dist=loadscope
```

* `--dist=loadscope` → ensures tests from the same module/class run in the same worker (good if you have shared setup/teardown).
* `--dist=load` → fully random distribution (better for performance, but riskier if tests depend on shared state).

---

## ⚠️ Things to watch out for

* Parallel tests must be **independent** (no shared DB/file state unless isolated).
* If using temporary files, use `tmp_path` fixture to avoid clashes.
* For API tests, make sure test data (like `POST` → `DELETE`) doesn’t interfere across workers.

---

👉 Do you want me to also show you how to **combine parallel execution with markers** (e.g., run only `api` tests in parallel while skipping slow ones)?

-------
Great question 🙌 — in `pytest` you can **focus on only specific tests** or **skip certain tests**. Here’s how you do both:

---

# ✅ Run Only Specific Tests

### 1. Using `-k` (keyword expression)

Run tests whose names match a keyword:

```bash
pytest -k "login"
```

👉 Runs all tests with `"login"` in the name.

---

### 2. Run a specific test function

```bash
pytest test_file.py::test_function_name
```

Or inside a class:

```bash
pytest test_file.py::TestClass::test_method
```

---

### 3. Mark a test with `@pytest.mark.only` (custom trick)

`pytest` doesn’t have built-in `.only` like JavaScript’s Jest/PactumJS, but you can simulate it:
refer: https://docs.pytest.org/en/stable/how-to/mark.html
```python
import pytest

@pytest.mark.only
def test_focus_this():
    assert 1 + 1 == 2

def test_other():
    assert 2 + 2 == 4
```

Run only tests with that mark:

```bash
pytest -m only
```

---

# 🚫 Skip Tests

### 1. Skip using decorator

```python
import pytest

@pytest.mark.skip(reason="Feature not ready yet")
def test_future_feature():
    assert False
```

---

### 2. Skip conditionally

```python
import sys
import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_not_on_windows():
    assert True
```

---

### 3. Dynamically skip inside a test

```python
import pytest

def test_dynamic_skip():
    if True:  # some condition
        pytest.skip("Skipping due to unmet condition")
    assert 1 == 1
```

---

# ⚡ Pro tip

* Use `pytest -rs` to **see skip reasons** in the report.
* You can combine: run only some tests while skipping others.

---

👉 Do you want me to also show you how to **mark tests as “slow”** and skip them by default (but run only when you explicitly ask for `--runslow`)?

Perfect question 🙌 — **fixtures are one of pytest’s most powerful features**, and understanding them well makes your test suites **cleaner, faster, and reusable**. Let’s break it down:

---

# 🔹 What is a Fixture in pytest?

A **fixture** is a function that provides test functions (or test classes) with some *setup resources*.

* Think of it as a **dependency injector**.
* Examples: database connection, API client, test data, temp files.
* Instead of writing setup code in every test, you define a fixture once, and pytest automatically passes it where needed.

---

# 🔹 Basic Example

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_name(sample_data):
    assert sample_data["name"] == "Alice"

def test_age(sample_data):
    assert sample_data["age"] == 30
```

👉 `sample_data` fixture is injected into both tests automatically.

---

# 🔹 Fixture Scopes

You can control **how often a fixture runs** with `scope`.

* `function` (default) → runs fresh for each test.
* `class` → runs once per class of tests.
* `module` → runs once per test file.
* `session` → runs once per entire test run.

Example:

```python
@pytest.fixture(scope="module")
def db_connection():
    print("\nSetting up DB")
    yield {"db": "connected"}
    print("\nTearing down DB")
```

* `yield` → lets you define **setup** (before yield) and **teardown** (after yield).
* Runs only **once for the module**.

---

# 🔹 Using `autouse` Fixtures

If you don’t want to **explicitly request** a fixture, you can make it run automatically:

```python
@pytest.fixture(autouse=True)
def setup_logging():
    print("\nLogging initialized")
```

👉 This will run for **every test automatically**.

---

# 🔹 Fixtures in Classes

```python
class TestAPI:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        self.client = {"name": "API Client"}

    def test_client_has_name(self):
        assert self.client["name"] == "API Client"
```

👉 The `setup_client` fixture runs before each method in the class, initializing `self.client`.

---

# 🔹 Parametrized Fixtures

You can run the same test with multiple fixture values:

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_number_is_positive(number):
    assert number > 0
```

👉 Runs the test **3 times**: with `1`, `2`, and `3`.

---

# 🔹 Fixture Dependency (Fixtures Using Fixtures)

Fixtures can **depend on other fixtures**:

```python
@pytest.fixture
def user_id():
    return 42

@pytest.fixture
def user_profile(user_id):
    return {"id": user_id, "name": "Alice"}

def test_user_profile(user_profile):
    assert user_profile["id"] == 42
```

👉 `user_profile` depends on `user_id`, and pytest resolves this automatically.

---

# 🔹 Example: API Client with Setup/Teardown

```python
import pytest
import requests

BASE_URL = "https://reqres.in/api"

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    yield session
    session.close()

def test_get_users(api_client):
    response = api_client.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
```

👉 `api_client` is created once per session, reused in all tests, and cleaned up after.

---

# ✅ Summary of Fixtures

* **Keep tests DRY** (don’t repeat setup code).
* **Scalable**: one fixture can power many tests.
* **Reusable**: can depend on other fixtures.
* **Flexible**: support parametrization, autouse, and different lifetimes (scopes).

---

👉 Fixtures are the **#1 reason pytest is preferred over unittest** — they let you design **clean, modular, and maintainable** tests.

Would you like me to also create a **cheat sheet PDF with all pytest fixture patterns** (basic, scope, autouse, parametrization, dependency) for quick reference?

```bash
pytest --junitxml=reports/junit-report.xml
```

```bash
python split_junitxml.py reports/junit-report.xml reports/output.xml
```