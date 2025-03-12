import sys
import os

# Add the project root directory to sys.path so we can import `art`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from art import get_art

def test_generate_ascii_art():
    art = get_art()
    assert isinstance(art, str)  # Ensure output is a string
    assert len(art.strip()) > 0  # Check to make sure art is not empty
