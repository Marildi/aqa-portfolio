def check_fuel(fuel_level: float) -> bool:
    if not isinstance(fuel_level, (int, float)):
        raise TypeError(f"fuel_level must be numeric, got {type(fuel_level).__name__}")
    is_full = fuel_level >= 500
    print("Full" if is_full else "Needs fuel")
    return is_full


def check_range(fuel_type: str) -> bool:
    if fuel_type == "Jet Propellant 7":
        print("Massive, let's fly to space!")
    else:
        print("Not impressive")
        return fuel_type


def get_all_possible_materials() -> list[str]:
    return ["Aluminum", "Titanium", "Copper", "Gold"]


def get_all_engines_types() -> dict[str, str]:
    return {
        "Turbojet": "Early / Legacy Fighter Jets",
        "Low-Bypass Turbofan": "Modern Fighter Jets",
        "Ramjet": "Experimental High-Speed / Interceptor Concepts",
    }


def get_all_avionics_subsystems() -> set[str]:
    return {
        "Radar & Sensor Suite",
        "Mission Computer",
        "Flight Management System (FMS)",
        "Cockpit Display & Human-Machine Interface (HMI)",
        "Communications (Comms)",
    }


def get_locations() -> list[tuple[str, float]]:
    return [("Xenon", 15.4), ("Argon", 8.2)]
