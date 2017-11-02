# Exercise 19 Study Drill #3
# Making a basic eccentricity calculator using apoapsis & periapsis!
# Here we're defining our function and giving it some calculations to perform:
def GEO_e_calc(apoapsis, periapsis):
    eccentricity = round(abs(1 - (2 / ((int(periapsis) / int(apoapsis)) + 1))),5)
    print(f"If your apoapsis is {apoapsis}km, and your periapsis is {periapsis}km, assuming an elliptical orbit...")
    print(f"Your eccentricity ratio is {eccentricity}")

# Ask user for values
print("What's the apoapsis of your orbit (in km)?")
apoapsis = input("> ")
print("What's the periapsis of your orbit (in km)?")
periapsis = input("> ")

# Run function
GEO_e_calc(apoapsis, periapsis)
