import pytest

@pytest.fixture(scope="class")
def db_connection():
    print("\nSetup DB connection")
    yield {"db": "connected"}
    print("\nTeardown DB connection")

class TestDatabase:
    def test_insert(self, db_connection):
        assert db_connection["db"] == "connected"

    def test_query(self, db_connection):
        assert db_connection["db"] == "connected"
