# test_reqres_api.py
import requests

BASE_URL = "https://reqres.in/api"
headers = {"Content-Type": "application/json", 'x-api-key': 'reqres-free-v1'}

def test_list_users():
    """Test GET /users?page=2"""
    response = requests.get(f"{BASE_URL}/users?page=2", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert data["page"] == 2


def test_single_user():
    """Test GET /users/2"""
    response = requests.get(f"{BASE_URL}/users/2", headers=headers)
    assert response.status_code == 200
    user = response.json()["data"]
    assert user["id"] == 2
    assert "email" in user


def test_create_user():
    """Test POST /users"""
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"


def test_update_user():
    """Test PUT /users/2"""
    payload = {"name": "neo", "job": "the one"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "neo"
    assert data["job"] == "the one"


def test_delete_user():
    """Test DELETE /users/2"""
    response = requests.delete(f"{BASE_URL}/users/2", headers=headers)
    assert response.status_code == 204
    assert response.text == ""

# To run the tests, use the command: pytest -v test_reqres_api.py