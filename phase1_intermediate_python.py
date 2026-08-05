# #Step 13: Object-Oriented Python — classes, __init__, inheritance, super()
# # for info: 
# # A function is standalone, not attached to any class
# # A method is a function defined inside a class, and it operates on an instance via self

# #And Step 14: magic methods "dunder" (double underscore) — __str__, __repr__, __eq__

# #1. create a base class with __init__ and define print for it
# import time
# from utils.fuel_checks import check_range, check_fuel

# class FlyingObjects:

#     def __init__(self, category: str, speed: int):
#         self.category = category
#         self.speed = speed

#     def __str__(self):
#         return f"Category with __str__: {self.category}"

# # #2. methods for the class
#     def check_status(self):
#         print(f"{self.category} (speed {self.speed} km/h) is sent to collection facility.")

# uav = FlyingObjects("UAV", 80)
# uav.check_status()
# print("Category check: " + uav.category)
# print(uav)

# #3. subclass that inherits from base class
# #uses super().__init__(), and overrides or extends the parent's method
# class FighterJets(FlyingObjects):
#     def __eq__(self, other):
#         return self.category == other.category

#     def __repr__(self):
#         return f"Jet: {self.category}, {self.speed}"

#     def __init__(self, category: str, speed: int, material: str):
#         super().__init__(category, speed)
#         print(f"Is made of {self.material}.")

# new_fighter_jet = FighterJets("Fighter Jet", 3529, "Titanium")
# new_fighter_jet.check_status()
# print(new_fighter_jet.speed)
# print(new_fighter_jet)

# #__repr__
# fighter_jets = [FighterJets("long-range", 4000, "Titanium"), FighterJets("Short-range", 800, "Aluminum")]
# print(fighter_jets)

# #__eq__
# first_jet = FighterJets("One in category", 3000, "Titanium")
# second_jet = FighterJets("One in category", 3000, "Titanium")
# print(first_jet == second_jet)

# #Step 15: Modules and packages: imports __init__.py
# class AdvancedFighterJets(FighterJets):
#     def __init__(self, category: str, speed: int, material: str, fuel_type: str):
#         super().__init__(category, speed, material)
#         self.fuel_type = fuel_type

# sr_71 = AdvancedFighterJets("Long-range", 4000, "Titanium", "Jet Propellant 7")
# fuel_type = sr_71.fuel_type
# check_range(fuel_type)
# check_fuel(5000.66)

# #16: Decorators

# #timing decorator: Measure how long a function takes to run — spot slow tests/operations
# #import time is in the top of the document
# print("\nTiming Decorators:")

# def check_test_time_decorator(func):
#     def time_wrapper(*args, **kwargs):
#         start_test_time = time.time()
#         logged_test_time = func(*args, **kwargs)
#         end_test_time = time.time()
#         print(f"{func.__name__} executed {end_test_time - start_test_time:.4f} seconds")
#         return logged_test_time
#     return time_wrapper 

# #decorator for imported func
# check_fuel_time_decorator = check_test_time_decorator(check_fuel)

# #decorator for other tests
# @check_test_time_decorator	
# def check_registration():
#     time.sleep(5.07)
#     return "finished"

# @check_test_time_decorator
# def check_pass_reset():
#     time.sleep(5)
#     return "finished"

# check_registration()
# check_pass_reset()
# check_fuel_time_decorator(88.09)


# #logging decorator: Record when a function is called, with what arguments, and what it returned — for debugging/audit trails
# #for console result clarity
# print("\nLogging Decorators:")

# def logging_for_tests_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Processing {func.__name__} with args={args}, kwargs={kwargs}")
#         data = func(*args, **kwargs)   
#         print(f"{func.__name__}, result: {data}")
#         return data
#     return wrapper

# #reusing method used in time wrapper in logging
# record_logs_registration = logging_for_tests_decorator(check_registration)
# record_logs_registration()

# #defining new method for logging
# @logging_for_tests_decorator
# def method_for_logging(text: str):
#     return isinstance(text, str)

# method_for_logging("Key-word")
# print("\nRetry decorator")

# #retry decorator: Automatically re-run a function if it fails, up to N times — handles flaky operations (network calls, flaky tests)
# def retry_decorator(max_attempts=3):
#     def inside_decorator(func):
#         def wrapper_retry(*args, **kwargs):
#             for attempt in range(1, max_attempts + 1):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Attempt {attempt} is failed: {e}")
#             raise Exception(f"Max {max_attempts} is reached, status: failed")
#         return wrapper_retry
#     return inside_decorator

# @retry_decorator(max_attempts=3)
# def func_poor_network():
#     import random
#     if random.random() < 0.7:
#         raise ConnectionError("Connection failed")
#     return "Connection established"

# func_poor_network()

#Step 17: Context managers — with statements, writing own using __enter__/__exit__
#custom context manager class, logs entry/exit
# import json


# class SuiteProcessing:
#     def __init__(self, filename):
#         self.filename = filename

#     #case 1: enter problem - a context manager's safety net - script finishes if the error ocurred in the __enter__ block. Json file has a comment in the beginning of the file
#     # def __enter__(self):
#     #     self.file = open(self.filename, "r")   # open the actual file
#     #     data_from_file = json.load(self.file)   # json.load (no "s") reads directly from a file object
#     #     print(data_from_file)
#     #     return data_from_file

#     #case 2: close the file in the enter, then crash the exit logic - won't crash because it's deliberate design choice in Python, it will call the second close() silently
#     def __enter__(self):
#             self.file = open(self.filename, "r")   # open the actual file
#             data_from_file = json.load(self.file)   # json.load (no "s") reads directly from a file object
#             print(data_from_file)
#             self.file.close()

#     #case 3: trigger an error in exit
#     #io.UnsupportedOperation: not writable - would show this error if file wasn't already closed in the __enter__ block
#     def __exit__(self, exc_type, exc, tb):
#         self.file.write("\n# processed")   # this WILL fail - file was opened in "r" mode
#         self.file.close()
#         if exc_type is not None:
#             print(f"Error occurred: {exc}")
#         return False

# with SuiteProcessing("cases.json") as f:
#     print("finished")

# #Step 18: Generators and yield — lazy evaluation
# def read_large_json(filename):
#     with open(filename, "r") as f:
#         for line in f:
#             yield line.strip()

# xenon_lines = (line for line in read_large_json("cases.json") if "Xenon" in line)

# print(next(xenon_lines))
# print(next(xenon_lines))

#Step 19: Type hints (typing module) 
#added hints in the fuel_checks.py

# from utils.fuel_checks import (
#     get_all_avionics_subsystems,
#     get_all_engines_types,
#     get_all_possible_materials,
#     get_locations,
# )

# print(get_all_possible_materials())
# print(get_locations())
# print(get_all_engines_types())
# print(get_all_avionics_subsystems())


#Step 20: requirements.txt vs pyproject.toml, currently using .toml, added uv add --dev pytest

#Step 21: Regular expressions (re module) — log-parsing practice
import re

#Find all lines containing ERROR
print("ERRORS:")
with open("mobile_app_crash.txt", "r") as logs_file:
       logs_records = logs_file.readlines()
       for line in logs_records:
          all_lines_with_errors = re.findall("ERROR", line)
          if all_lines_with_errors:
               print(line)


#Extract all timestamps from the log
print("ALL TIMESTAMPS:")
for line in logs_records:
     all_timestamps = re.findall(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})", line)
     if all_timestamps:
          print(line.strip())


print("\n") #for terminal view

#Extract the severity level and message separately using capture groups
import re
from enum import IntEnum


class Severity(IntEnum):
    FATAL = 1
    ERROR = 2
    WARN = 3
    INFO = 4
    DEBUG = 5

     #1. temporary container to collect the matches (because regex can't be sorted directly)
collected_matches = []

pattern = r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\] \[(\w+)\] \[(\w+)\] (.*)"

     # 2. Extract and store the data fields
for line in logs_records:
     errors_data = re.search(pattern, line)
     if errors_data:
          level, agent, explanation = errors_data.groups()
          # Store them grouped together as a tuple inside our list
          collected_matches.append((level, agent, explanation))

     # 3. Sort the collected list based on SEVERITY_PRIORITY 
     # (row[0] checks the 'level' string like "INFO" or "ERROR" against  map)
collected_matches.sort(key=lambda row: Severity[row[0]])

     # 4. Print out final sorted data
print("SEVERITY LEVELS (SORTED):")
for level, agent, explanation in collected_matches:
     print(f"Level: {level} | Agent: {agent} | Message: {explanation}")


print("\n")
  
#Redact something sensitive (like an IP address or an ID) using re.sub()
import re

# Used parentheses () to create a capture group for "User ID: " so we can keep it
pattern_id = r"(User\s+ID:\s*)(\d+)"
extracted_lines = []

with open("mobile_app_crash.txt", "r", encoding="utf-8") as file:
    for line in file:
        if re.search(pattern_id, line):
            extracted_lines.append(line.strip())

# Loop through and mask every extracted line
for match_line in extracted_lines:
    # \1 pulls back the text from the first capture group (User ID: ) 
    # and only replaces the digits with XXXXXX
    masked_line = re.sub(pattern_id, r"\1XXXXXX", match_line)
    print(masked_line)
