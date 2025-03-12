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

def test_home_html(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Automated Testing Demo!" in response.data  # Check if HTML contains expected text
