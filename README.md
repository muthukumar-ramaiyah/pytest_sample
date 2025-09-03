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
