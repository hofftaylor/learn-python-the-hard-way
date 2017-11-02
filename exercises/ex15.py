# Exercise 15 - Reading Files

# Step one, load argv from the sys module.
from sys import argv

# Step two, set the filename as the argument we'll need from the user at the command line.
script, filename = argv

# Step three, set the variable txt to be the contents of the filename we specified, which is opened by that eponymous command.
txt = open(filename)

# Step four, print a formatted string and then print out the contents of the variable we set earlier.
print(f"Here's your file {filename}:")
print(txt.read())

# Step five, prompt the user for another filename and set that to file_again variable.
print("Type the filename again:")
file_again = input("> ")

# Step six, take that file and set it's contents to the variable txt_again.
txt_again = open(file_again)

# Step seven, print that variable's contents.
print(txt_again.read())

# Step eight, close all the files we opened
txt.close()
txt_again.close()
