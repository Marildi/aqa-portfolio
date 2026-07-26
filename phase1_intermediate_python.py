#Step 13: Object-Oriented Python — classes, __init__, inheritance, super()
# for info: 
# A function is standalone, not attached to any class
# A method is a function defined inside a class, and it operates on an instance via self

#And Step 14: magic methods "dunder" (double underscore) — __str__, __repr__, __eq__

#1. create a base class with __init__ and define print for it
from utils.fuel_checks import check_range, check_fuel

class FlyingObjects:

    def __init__(self, category: str, speed: int):
        self.category = category
        self.speed = speed

    def __str__(self):
        return f"Category with __str__: {self.category}"

#2. methods for the class
    def check_status(self):
        print(f"{self.category} (speed {self.speed} km/h) is sent to collection facility.")

uav = FlyingObjects("UAV", 80)
uav.check_status()
print("Category check: " + uav.category)
print(uav)

#3. subclass that inherits from base class
#uses super().__init__(), and overrides or extends the parent's method
class FighterJets(FlyingObjects):
    def __eq__(self, other):
        return self.category == other.category

    def __repr__(self):
        return f"Jet: {self.category}, {self.speed}"

    def __init__(self, category: str, speed: int, material: str):
        super().__init__(category, speed)
        self.material = material
    def check_status(self):
        super().check_status()
        print(f"Is made of {self.material}.")

new_fighter_jet = FighterJets("Fighter Jet", 3529, "Titanium")
new_fighter_jet.check_status()
print(new_fighter_jet.speed)
print(new_fighter_jet)

#__repr__
fighter_jets = [FighterJets("long-range", 4000, "Titanium"), FighterJets("Short-range", 800, "Aluminum")]
print(fighter_jets)

#__eq__
first_jet = FighterJets("One in category", 3000, "Titanium")
second_jet = FighterJets("One in category", 3000, "Titanium")
print(first_jet == second_jet)

#Step 15: Modules and packages: imports __init__.py
class AdvancedFighterJets(FighterJets):
    def __init__(self, category: str, speed: int, material: str, fuel_type: str):
        super().__init__(category, speed, material)
        self.fuel_type = fuel_type

sr_71 = AdvancedFighterJets("Long-range", 4000, "Titanium", "Jet Propellant 7")
fuel_type = sr_71.fuel_type
check_range(fuel_type)
check_fuel(5000.66)

