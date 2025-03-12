# tests/test_flask_app.py

import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')  # Changed from /hello to /
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}
