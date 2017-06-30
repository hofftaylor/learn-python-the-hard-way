# Exercise 11 - Asking Questions

#Printing a question and using end = ' ' to not end it with a newline character \n and instead go to the next line.
print("How old are you?", end=' ')
#Asking it to take whatever string we provide and set it to the variable age.
age = input()
print("How tall are you in centimeters?", end=' ')
height = input()
print("How much do you weigh in pounds?", end=' ')
weight = input()

#Printing a formatted string with the variables we just set.
print(f"So you're {age} years old, {height} cm tall, and {weight} lbs heavy.")

#This prompts for input using a string, and then converts that input into an integer and sets that integer to a variable. WHOOOOO NOW WE'RE COOKIN WITH GAS!!!!!!
sleep = int(input("How many hours of sleep did you get last night? "))

#OHHHH SHIT LOGIC TIME, if variable sleep is less than 6, print the indented formatted string (Why it needed to be indented I have no idea... yet.)
if sleep < 6:
    print(f"Only {sleep} hours? That's not a lot. You should sleep more.")
#This one is tricky, it asks if the integer 6 is less than or equal to the variable sleep and that if variable sleep is less than or equal to integer 7, then print this formatted string. Basically we want anything between 6 and 7 to result in this string printing.
if 6 <= sleep <= 7:
    print(f"{sleep} hours? Not bad! But make sure you get at least 8 hours a night!")
#If the variable sleep is 8, we print this message.
if sleep == 8:
    print(f"{sleep} hours is the perfect amount! Keep it up!")
#If the variable sleep is greater than 8, we print this string!
if sleep > 8:
    print(f"{sleep} hours is too many! You can get that much sleep when you're dead.")
