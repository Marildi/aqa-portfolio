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

#LISTS
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

#FUNCTIONS
#Basic function
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

#LIST/DICT COMPREHENSIONS
#Basic list
# male_guests = ["Goodchild", "Bashire"]     # list - ordered, allows duplicates
# male_guests = {"Goodchild", "Bashire"}     # set - unordered, unique only
# male_guests = ("Goodchild", "Bashire")     # tuple - ordered, immutable


male_guests = ("Goodchild", "Bashire")
female_guests = ("Flux", "Tina")

prefixes = ["Mr " + surname for surname in male_guests]
print(prefixes)

fprefixes = ["Mrs " + surname for surname in female_guests]
print(fprefixes)


#List comprehension with a filter
db = ["Di", "Scarlett", "Jetta"]
short_names = [name for name in db if len(name) <=5]
print(short_names)

#Dict comprehension
failed_tests = ["login", "reset_pass", "delete_acc"]
passed_tests = ["change_role", "add_new_user"]
fail_results = {test:"fail" for test in failed_tests}
pass_results = {test: "pass" for test in passed_tests}

print(fail_results)
print(pass_results)

#List that transforms strings
capital_letters_names = ["MITCHELL", "MARTINS"]
adjusted_names = [name.lower() for name in capital_letters_names]
print(adjusted_names)
