# Exercise 5 - More Variables and Printing

# We're going to make a bunch of strings in this exercise. However, we first start by setting a bunch of variables to both strings and values.

# We're gonna set this first variable to a string.
name = 'Zed A. Shaw'
# These next three variables we set to some values.
age = 35 # not a lie
height_in = 74 # weight in inches
weight_lbs = 180 # weight in pounds
# And these next three variables we set as strings.
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# Converting lbs to kg
weight_kg = 0.45359237 * weight_lbs
# Converting in to cm
height_cm = 2.5400 * height_in

# Now we're going to display these variables inside of some strings.
print(f"Let's talk about {name}.")
print(f"He's {height_in} inches tall.")
print(f"(That's {height_cm} centimeters tall for you non-heathens.)")
print(f"He's {weight_lbs} pounds heavy.")
print(f"(That's {weight_kg} kilos heavy for you non-heathens.)")
print("Either way you measure it, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky but we're baller so here goes... Calculate these arbitrary variables and set them to other variables! DO IT!
total = age + height_in + weight_lbs
metrictotal = age + height_cm + weight_kg

print(f"If I add {age}, {height_in}, and {weight_lbs} I get {total}.")
print(f"And if I add {age}, {height_cm}, and {weight_kg} I get {metrictotal}.")
print("Naturally, none of this math makes sense. None of these units go together. But whatever! Learning!!")

# Addendum - A mini test of line order and unit conversions!
# Whelp. That didn't work. Moved those values up in the proper line order. Turns out that order DOES matter in programming! Crazy!
