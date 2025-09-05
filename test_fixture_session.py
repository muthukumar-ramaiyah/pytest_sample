import pytest

import pytest
import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {"Content-Type": "application/json", 'x-api-key': 'reqres-free-v1'}

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update(HEADERS)
    yield session
    session.close()

def test_get_users(api_client):
    response = api_client.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
