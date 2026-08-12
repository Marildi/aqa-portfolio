# tests/conftest.py
import os

import pytest


@pytest.fixture
def temp_results_file():
    filename = "temp_file.csv"
    with open(filename, "w") as f:
        f.write("test_name,status\n")
        f.write("test_login,Passed\n")
        f.write("test_logout,Failed\n")
    yield filename
    os.remove(filename)
