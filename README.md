# Weekly Assignment 2

This project contains solutions for Weekly Assignment 2 in Python, with both unit tests and integration tests written using `pytest` and `pytest-mock`.

#### Create environment and install dependencies
    python3 -m venv .venv
    source .venv/bin/activate
    pip install pytest pytest-mock   
    pip install -r requirements.txt

#### Run all tests:
    pytest

#### Run only unit tests: 
    pytest -m unit

#### Run only integration tests: 
    pytest -m integration

## Project structure

```text
src/
tests/
  unit/
  integration/