import pytest

@pytest.fixture(autouse=True)
def setup_logging():
    print("\nLogging initialized")

from my_math import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5