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
#Need order + duplicates + changeable -> list
domains = ["cybersecurity", "plasma physics", "nuclear physics", "metals science"]
print(domains[0])

#Need order + fixed, unchangeable → tuple
metals = ("aluminum", "titanium", "gold", "copper")
#print(metals)
metals[0]="flower" #should throw an error test

#Need labeled lookup (like JSON) → dict
pressureIndicators= {
    "green":"low",
    "yellow":"moderate",
    "red":"high"
}
print(pressureIndicators["green"])

#Need uniqueness only → set
teams = {"supply_chain", "cyber_IT", "cyber_OT", "systems_engineers"}
if "cyber_IT" in teams:
    print("On the list!")