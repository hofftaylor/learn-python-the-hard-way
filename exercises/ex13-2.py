# Example 13-2 , A real example!

# Importing what we need from sys module
from sys import argv

# Setting unpacking variables to argv
script, numerator, denominator = argv

# Asking the user if they want sig figs
sigfigs = input("Do you want sig figs with that? ")

# Doing math!
answer = int(numerator) / int(denominator)

# Using our sigfigs answer to conditionally print the answer
if sigfigs == "yes":
    print("The divid-o-matic takes your two numbers, and PRESTO!")
    print(f"{numerator} / {denominator} = {answer}")
if sigfigs == "no":
    print("The divid-o-matic takes your two numbers, and PRESTO!")
    print(f"{numerator} / {denominator} = {int(answer)}")
