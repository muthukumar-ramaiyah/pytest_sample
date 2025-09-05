import pytest

@pytest.fixture
def user_id():
    return 42

@pytest.fixture
def user_profile(user_id):
    return {"id": user_id, "name": "Alice"}

def test_user_profile(user_profile):
    assert user_profile["id"] == 42
