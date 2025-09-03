# test_my_math_pytest.py
from my_math import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5
# To run the tests, use the command: pytest pytest_my_math.py
# or simply: pytest
# Ensure pytest is installed in your environment.
# You can install it using pip if you haven't already:
# pip install pytest
# pytest will automatically discover and run the test functions prefixed with 'test_'
# in the specified file or in the current directory if no file is specified.
# The output will show the results of the tests, indicating any failures or errors.
# For more detailed output, you can use the -v (verbose) option:
# pytest -v pytest_my_math.py
# This will provide more information about each test that was run.
# You can also run all tests in the current directory and its subdirectories by simply running:
# pytest
