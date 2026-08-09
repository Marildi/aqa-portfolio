from utils.fuel_checks import check_fuel


# Equivalence partitioning
def test_check_fuel_clearly_above_threshold():
    assert check_fuel(550)


def test_check_fuel_clearly_below_threshold():
    assert not check_fuel(10)


# Boundary value analysis
def test_check_fuel_at_boundary():
    assert check_fuel(500)


def test_check_fuel_just_below_boundary():
    assert not check_fuel(499.99)


def test_check_fuel_just_above_boundary():
    assert check_fuel(500.01)


# Invalid/negative input
def test_check_fuel_zero():
    assert not check_fuel(0)


def test_check_fuel_negative():
    assert not check_fuel(-50)
