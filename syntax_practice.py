# rocketName = "Atlantis"
# totalRocketWeight = 2000.55
# fuelWeight = 1500
# isInOrbit = False

# # rocketWeight = totalRocketWeight - fuelWeight
# # print(f"The {rocketName} weights {rocketWeight}, fuel weight is {fuelWeight}")

# # hasEnoughFuel = fuelWeight > 1000
# # print(f"Enough fuel: {hasEnoughFuel}, in orbit: {isInOrbit}")

# #if

# if not isInOrbit:
#     print("Atlantis not in orbit")
# else:
#     print("Already left")

# fuelPercent = 45


# #elif - multiple conditions

# if fuelPercent > 80:
#     print("Fuel: full")
# elif fuelPercent >30:
#     print("Fuel: moderate")
# else:
#     print("Fuel: critical")

# #for loop

# systems = ["navigation", "engine", "life_support"]
# for item in systems:
#     print(f"Checking {item}")

# #while loop - runs until condition is false
# countdown = 5
# while countdown > 0:
#     print(countdown)
#     countdown -=1

# #break and continue

# for system in systems:
#     if system == "navigation":
#         continue
#     if system == "life_support":
#         break
#     print(f"Testing {system}")

# LISTS
# #Need order + duplicates + changeable -> list
# domains = ["cybersecurity", "plasma physics", "nuclear physics", "metals science"]
# print(domains[0])

# #Need order + fixed, unchangeable → tuple
# metals = ("aluminum", "titanium", "gold", "copper")
# #print(metals)
# # metals[0] = "flower"  # tuples are immutable — this line is commented out since it would throw TypeError

# #Need labeled lookup (like JSON) → dict
# pressureIndicators= {
#     "green":"low",
#     "yellow":"moderate",
#     "red":"high"
# }
# print(pressureIndicators["green"])

# #Need uniqueness only → set
# teams = {"supply_chain", "cyber_IT", "cyber_OT", "systems_engineers"}
# if "cyber_IT" in teams:
#     print("On the list!")

# FUNCTIONS
# Basic function
# def check_security_code(securityCodeWord):
#     return securityCodeWord == "Atlantis"

# print(check_security_code("Poseidon"))

# def check_pilots_count(number):
#     return number > 1

# print(check_pilots_count(4))


# #dosctrings
# def check_security_code_advanced(securityCodeWord: str) -> bool:
#     """Return True if the given security code matches 'Atlantis'."""
#     return securityCodeWord == "Atlantis"

# #Default arguments
# def check_max_distance(distance, threshold=1000):
#     return distance > threshold

# print(check_max_distance(11000))
# print(check_max_distance(999))


# #*args
# def check_every_pilot_identity(*pilots):
#     for pilot in pilots:
#         print(f"{pilot} is confirmed")

# check_every_pilot_identity("Goodchild", "Chuck", "Mitch", "Dakota")

# #*kwargs
# def report_shell_temperature(**degrees):
#     for star_proximity, value in degrees.items():
#         print(f"{star_proximity}: {value}")

# report_shell_temperature(three_hundred=37, two_hundred=84, one_hundred=116)

# #return types with type hints
# def is_weight_maximum_reached(amount:float):
#     return amount >= 50.57

# print(is_weight_maximum_reached(50.56))

# LIST/DICT COMPREHENSIONS
# Basic lists
# male_guests = ["Goodchild", "Bashire"]     # list - ordered, allows duplicates
# male_guests = {"Goodchild", "Bashire"}     # set - unordered, unique only
# male_guests = ("Goodchild", "Bashire")     # tuple - ordered, immutable

# Basic list comprehension
# male_guests = ("Goodchild", "Bashire")
# female_guests = ("Flux", "Tina")

# prefixes = ["Mr " + surname for surname in male_guests]
# fprefixes = ["Mrs " + surname for surname in female_guests]
# print(fprefixes)


# #List comprehension with a filter
# db = ["Di", "Scarlett", "Jetta"]
# short_names = [name for name in db if len(name) <=5]
# print(short_names)

# #Dict comprehension
# failed_tests = ["login", "reset_pass", "delete_acc"]
# passed_tests = ["change_role", "add_new_user"]
# fail_results = {test:"fail" for test in failed_tests}
# pass_results = {test: "pass" for test in passed_tests}

# print(fail_results)
# print(pass_results)

# #List that transforms strings
# capital_letters_names = ["MITCHELL", "MARTINS"]
# adjusted_names = [name.lower() for name in capital_letters_names]
# print(adjusted_names)

# File I/O — text, CSV, JSON
# import json
# import csv
# import re

# #a script that creates a small list of "test results" (dicts with test_name/status/duration)
# with open("test_results.txt", "w") as f:
#     f.write("test_name\nstatus\nduration\n")

# with open("test_results.txt", "r") as f:
#     data = f.read()
#     print("1.Txt file data:\n"+data)

# #parse txt to csv
# txt_filename = "test_results.txt"
# csv_filename = "test_results.csv"

# with open(txt_filename, "r", encoding="utf-8") as txt_file, \
# open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:

#     csv_writer = csv.writer(csv_file)

#     for line in txt_file:
#          # 1. Clean the line by removing trailing newlines/spaces
#         cleaned_line = line.strip()
#         # 2. Skip completely blank lines or divider lines (dashed lines)
#         if not cleaned_line or cleaned_line.startswith("-"):
#             continue
#         # 3. Split fields by 2 or more spaces to preserve names with single spaces
#         row = re.split(r'\s{2,}', cleaned_line)
#         # 4. Write the cleaned data row to the CSV file
#         csv_writer.writerow(row)

# print(f"2.Successfully converted '{txt_filename}' to '{csv_filename}'.")
# print("Data in CSV file:\n"+csv_filename+"\n")


# #create+ write new csv file
# with open("new_test_results.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["test_name", "status", "duration"])
#     writer.writerow(["test_login", "pass", "1.2"])
#     writer.writerow(["test_logout", "fail", "0.8"])

# #writes the same data to a JSON file
# data = {"test_name": "auth_test", "status": "fail", "duration": 18}
# with open("result.json", "w") as f:
#     json.dump(data, f, indent=2)

# #reads both back and prints them
# with open("new_test_results.csv", "r") as f:
#     reader = csv.reader(f)
#     print("Read CSV created manually without parsing:")
#     for row in reader:
#         print(row)


# with open("result.json", "r") as f:
#     loaded = json.load(f)
#     print(f"\nThe result for the last test is:"+loaded["status"])


# 12: exception handling — try/except/finally, custom exceptions.
# TRY/EXCEPT + CUSTOM EXCEPTION + CATCHING ANY EXCEPTION WITH 'as e:' + MULTIPLE EXCEPTIONS
import os

import jwt
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
JWT_ALGORITHM = "HS256"

customers_list_roles = [
    {"customer_id": "kejfbekf22mm_dddcfdf", "role": "partner"},
    {"customer_id": "jkdfdfdeed_6665", "role": "stakeholder"},
    {"customer_id": "sfthtrfg0022", "role": "investor"},
]

# tuple for Python runtime checking
ALLOWED_CUSTOMER_ROLES = ("partner", "stakeholder", "investor")

system_user = {"system_user_id": "kdfkdefabiefkkkkffiWe_dfe", "role": "admin"}


# custom exeception
class InvalidTokenRoleError(Exception):
    """Raised when a JWT is valid but the role claim is missing or unauthorized."""


# decode the role from the token
def get_role_from_bearer_token(auth_header: str) -> str:
    """
    Parses a Bearer token, verifies its signature, and extracts the user role.
    Raises a PermissionError if the token is missing, invalid, or expired.
    """
    # 1. Verify the header presence and 'Bearer ' format
    if not auth_header or not auth_header.startswith("Bearer "):
        raise PermissionError("Invalid or missing Authorization header prefix.")

    # 2. Extract the raw token string (removes 'Bearer ')
    token = auth_header.split(" ")[1]

    try:
        # 3. Decode the token using server's secret key
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])

        # 4. Extract and return the role attribute from the token payload
        user_role = payload.get("role")
        if not user_role:
            raise InvalidTokenRoleError("Token payload is missing a 'role' claim.")
        return user_role

    except jwt.ExpiredSignatureError:
        raise PermissionError("The provided token has expired.")
    except jwt.InvalidTokenError:
        raise PermissionError("The provided token is invalid or tampered with.")


def changeCustomerRole(requested_customer_id: str, new_role: str, auth_header: str):
    # check permissions for the system user
    try:
        current_sys_user_role = get_role_from_bearer_token(auth_header)
    except PermissionError as e:
        print(f"Access Denied: {e}")
        return

    if current_sys_user_role != "admin":
        print("Access denied: User is not an admin.")
        return

    # User is admin, proceed with changes
    # RUNTIME GUARD CLAUSE: Verify the incoming new_role is valid before looping
    if new_role not in ALLOWED_CUSTOMER_ROLES:
        print(f"Error: '{new_role}' is not a valid role options.")
        return

    # Process the update since the role is safe
    for customer in customers_list_roles:
        if customer["customer_id"] == requested_customer_id:
            customer["role"] = new_role
            print(f"Role is changed successfully to {new_role}")
            break
    else:
        print("Role not found (Customer ID matches nothing)")


# 4. GENERATING A VALID TOKEN FOR TESTING
system_user = {"system_user_id": "kdfkdefabiefkkkffiWe_dfe", "role": "admin"}

# Generate a fresh token signed with our static key
GENERATED_JWT = jwt.encode(system_user, SECRET_KEY, algorithm=JWT_ALGORITHM)
test_auth_header = f"Bearer {GENERATED_JWT}"

print("1. Check for JWT Generation:")
print(test_auth_header)

print("\n2. Customers list before:")
print(customers_list_roles)

print("\n3. Attempting Role Change:")
# Pass the freshly generated token that matches our SECRET_KEY
changeCustomerRole("kejfbekf22mm_dddcfdf", "stakeholder", test_auth_header)

print("\n4. Customers list after:")
print(customers_list_roles)

# Test with a deliberately broken token
bad_auth_header = "Bearer this.is.not.a.valid.jwt"
changeCustomerRole("kejfbekf22mm_dddcfdf", "stakeholder", bad_auth_header)


# FINALLY
try:
    f = open("test_users_list.csv", "x")
    data = f.write("text")
except FileExistsError:
    print("File already generated")
finally:
    print("Check completed")
