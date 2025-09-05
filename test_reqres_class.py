import pytest
import requests

BASE_URL = "https://reqres.in/api"

class TestUsersAPI:

    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users?page=2")
        assert response.status_code == 200
        assert "data" in response.json()

    def test_single_user(self):
        response = requests.get(f"{BASE_URL}/users/2")
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["id"] == 2
        assert "email" in data
