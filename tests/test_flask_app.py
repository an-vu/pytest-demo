# tests/test_flask_app.py

import pytest
import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')  
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}
