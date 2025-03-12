import pytest
import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_html(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Automated Testing Demo!" in response.data  # Check if HTML contains expected text

def test_generate_ascii_art_route(client):
    response = client.get('/generate')
    assert response.status_code == 200
    assert "ascii_art" in response.get_json()

def test_generate_ascii_art_button(client):
    """Simulate what the frontend button does by making an API call"""
    response = client.get('/generate')
    assert response.status_code == 200
    data = response.get_json()
    
    # Ensure the button click fetches valid ASCII art
    assert isinstance(data["ascii_art"], str)
    assert len(data["ascii_art"].strip()) > 0

