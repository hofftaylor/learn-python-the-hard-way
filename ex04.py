# Exercise 4

# First we're going to set some initial variables. In each line here we'll be setting each variable to it's corresponding value.
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

# Next we're going to set more advanced variables to correspond with math functions that utilize the initial variables' values.
# In this variable, we're subtracting the value of cars (100) by the value of drivers (30).
cars_not_driven = cars - drivers
# In this variable, we're setting the value of cars driven to the value of the variable drivers.
cars_driven = drivers
# In this variable, we're setting the value of carpool capacity to the value of the variable cars_driven multiplied by the value of the variable space_in_a_car.
carpool_capacity = cars_driven * space_in_a_car
# In this varaible, we're setting the value of average_passengers_per_car to the value of the variable passengers divided by the value of the variable cars_driven.
average_passengers_per_car = passengers / cars_driven

# Now that we've set our initial variables to their necessary values and defined the math for some more advanced variables, we're ready to display some information!
# Each variable we previously defined is either calculated (or simply displayed) by the print function.

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "passengers to carpool today.")
print("We need to put about", average_passengers_per_car, "people in each car.")

# Addendum - Explain this error:

# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# This error is caused by a spelling error in the variable 'car_pool_capacity'. It contains an extra underscore that it should not, causing the program to ask (or call) for a variable that has not been given to it (or defined). A similar mistake has been made with 'passenger' instead of 'passengers'
