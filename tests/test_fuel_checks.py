# import os

# import pytest

# from utils.fuel_checks import check_fuel


# # Equivalence partitioning
# def test_check_fuel_clearly_above_threshold():
#     assert check_fuel(550)


# def test_check_fuel_clearly_below_threshold():
#     assert not check_fuel(10)


# # Boundary value analysis
# def test_check_fuel_at_boundary():
#     assert check_fuel(500)


# def test_check_fuel_just_below_boundary():
#     assert not check_fuel(499.99)


# def test_check_fuel_just_above_boundary():
#     assert check_fuel(500.01)


# # Invalid/negative input
# def test_check_fuel_zero():
#     assert not check_fuel(0)


# def test_check_fuel_negative():
#     assert not check_fuel(-50)


# 33
# @pytest.fixture(scope="module")
# def temp_results_file():
#     filename = "temp_file.csv"
#     print("\nSetup: creating temp file")
#     with open(filename, "w") as f:
#         f.write("test_name,status\n")
#         f.write("test_login,Passed\n")
#         f.write("test_logout,Failed\n")
#     yield filename  # give the test just the filename/path
#     print("\nTeardown: deleting temp file")
#     os.remove(filename)  # cleanup


# def test_file_contains_failed_status(temp_results_file):
#     with open(temp_results_file, "r") as f:
#         content = f.read()
#     assert "Failed" in content


# def test_file_contains_passed_status(temp_results_file):
#     with open(temp_results_file, "r") as f:
#         content = f.read()
#     assert "Passed" in content

# 34
import pytest

from utils.fuel_checks import check_fuel


@pytest.mark.parametrize(
    "fuel_level, expected",
    [
        (550, True),
        (10, False),
        (499.99, False),
        (500, True),
        (500.01, True),
        (0, False),
        (-50, False),
    ],
    ids=[
        "clearly_above",
        "clearly_below",
        "just_below_boundary",
        "at_boundary",
        "just_above_boundary",
        "zero",
        "negative",
    ],
)
def test_check_fuel(fuel_level, expected):
    assert check_fuel(fuel_level) == expected
