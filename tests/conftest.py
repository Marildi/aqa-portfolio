# tests/conftest.py
# import os

import pytest

# @pytest.fixture
# def temp_results_file():
#     filename = "temp_file.csv"
#     with open(filename, "w") as f:
#         f.write("test_name,status\n")
#         f.write("test_login,Passed\n")
#         f.write("test_logout,Failed\n")
#     yield filename
#     os.remove(filename)


# this version is for parallelism
@pytest.fixture(scope="module")
def temp_results_file(tmp_path_factory):
    filename = tmp_path_factory.mktemp("data") / "temp_file.csv"
    with open(filename, "w") as f:
        f.write("test_name,status\n")
        f.write("test_login,Passed\n")
        f.write("test_logout,Failed\n")
    yield filename
    # no manual cleanup needed - pytest cleans up tmp_path directories automatically
