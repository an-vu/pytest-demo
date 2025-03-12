# pytest-demo

Automated Testing Tool Demo Using pytest.

This repository demonstrates how to write and run automated tests using pytest in Python.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/pytest-demo.git
   cd pytest-demo
   ```
   
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```
   
3. Install dependencies:
   ```bash
   pip install pytest
   ```

## Running Tests
Run tests with:
```bash
pytest
```

## Example Test

Below is an example test case from this repo:

```python
from app.calculator import add

def test_add():
    assert add(2, 3) == 5
```
