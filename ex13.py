# Exercise 13 - Parameters, Unpacking, Variables

# First thing we do is tell python that we are going to use the argv command from the sys module (library?)
from sys import argv
# read the WYSS section for how to run this
# we are "unpacking" three arguments and assigning them to variables.
script, first, second, third = argv

# and now we're printing them
print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
