def check_fuel(fuel_level: float):
    if fuel_level >= 500:
        print("Full")
    else: 
        print("Needs fuel")


def check_range(fuel_type: str):
    if fuel_type == "Jet Propellant 7":
        print("Massive, let's fly to space!")
    else:
        print("Not impressive")