import pytest
from my_math import add

@pytest.fixture
def sample_data():
    return [ (2, 3, 5), (-1, -1, -2), (0, 5, 5) ]

def test_add(sample_data):
    for x, y, result in sample_data:
        assert add(x, y) == result

# Or parametrize directly
@pytest.mark.parametrize("x,y,result", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 5, 5),
])
def test_add_param(x, y, result):
    assert add(x, y) == result
# To run the tests, use the command: pytest test_my_math_pytest2.py
# or simply: pytest
# Ensure pytest is installed in your environment.