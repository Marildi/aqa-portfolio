#Step 13: Object-Oriented Python — classes, __init__, inheritance, super()
# for info: 
# A function is standalone, not attached to any class
# A method is a function defined inside a class, and it operates on an instance via self

#And Step 14: magic methods "dunder" (double underscore) — __str__, __repr__, __eq__

#1. create a base class with __init__ and define print for it
import time
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

#for console result clarity
print("\nTiming Decorators:")

#16: Decorators
#timing decorator: Measure how long a function takes to run — spot slow tests/operations
#import time is in the top of the document

def check_test_time_decorator(func):
    def time_wrapper(*args, **kwargs):
        start_test_time = time.time()
        logged_test_time = func(*args, **kwargs)
        end_test_time = time.time()
        print(f"{func.__name__} executed {end_test_time - start_test_time:.4f} seconds")
        return logged_test_time
    return time_wrapper 

#decorator for imported func
check_fuel_time_decorator = check_test_time_decorator(check_fuel)

#decorator for other tests
@check_test_time_decorator	
def check_registration():
    time.sleep(5.07)
    return "finished"

@check_test_time_decorator
def check_pass_reset():
    time.sleep(5)
    return "finished"

check_registration()
check_pass_reset()
check_fuel_time_decorator(88.09)


#logging decorator: Record when a function is called, with what arguments, and what it returned — for debugging/audit trails
#for console result clarity
print("\nLogging Decorators:")

def logging_for_tests_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Processing {func.__name__} with args={args}, kwargs={kwargs}")
        data = func(*args, **kwargs)   
        print(f"{func.__name__}, result: {data}")
        return data
    return wrapper

#reusing method used in time wrapper in logging
record_logs_registration = logging_for_tests_decorator(check_registration)
record_logs_registration()

#defining new method for logging
@logging_for_tests_decorator
def method_for_logging(str: str):
    print(str)
    return str == str

method_for_logging("Key-word")
print("\nRetry decorator")

#retry decorator: Automatically re-run a function if it fails, up to N times — handles flaky operations (network calls, flaky tests)
def retry_decorator(max_attempts=3):
    def inside_decorator(func):
        def wrapper_retry(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} is failed: {e}")
            raise Exception(f"Max {max_attempts} is reached, status: failed")
        return wrapper_retry
    return inside_decorator

@retry_decorator(max_attempts=3)
def func_poor_network():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Connection failed")
    return "Connection established"

func_poor_network()

