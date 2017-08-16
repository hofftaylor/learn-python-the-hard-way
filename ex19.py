# Exercise 19 - Functions and Variables
# Creating a function named "cheese_and_crackers" and which uses the arguments we gave it and then prints their values into a formatted string.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")
# Assigning the function some numbers directly as arguments, and calling the function.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
# Setting global variables with values to provide to the function
print("OR, We can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# Calling the function with the aformentioned variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# Doing math as arguments for the function.
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# Using variables combined with math inside of the function.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
