import pytest
import sys

@pytest.mark.only
def test_focus_this():
    assert 1 + 1 == 2

def test_other():
    assert 2 + 2 == 4

@pytest.mark.skip(reason="Feature not ready yet")
def test_future_feature():
    assert False

# To run the tests, use the command: pytest -v test_only_skip_pytest.py -m "not only"
# or simply: pytest -v test_only_skip_pytest.py

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_not_on_windows():
    assert True
# To run the tests, use the command: pytest -v test_only_skip_pytest.py
# or simply: pytest -v test_only_skip_pytest.py

def test_dynamic_skip():
    if True:  # some condition
        pytest.skip("Skipping due to unmet condition")
    assert 1 == 1

# To run the tests, use the command: pytest -v test_only_skip_pytest.py
# or simply: pytest -v test_only_skip_pytest.py
# Use pytest -rs to see skip reasons in the report.
# or simply: pytest -v test_only_skip_pytest.py -rs