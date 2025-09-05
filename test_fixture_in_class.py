import pytest

class TestAPI:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        self.client = {"name": "API Client"}

    def test_client_has_name(self):
        assert self.client["name"] == "API Client"
