# Exercise 16 - Reading and Writing Files
# Importing functions argv from library sys
from sys import argv
# Setting the functions we're pulling froma argv?
script, filename = argv
# Printing info for the user and formatting the strings.
print(f"We're going to erase {filename}.")
print("If you don't want to do that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# Asking the user: "Hey user, what do ya wanna do?"
input("?")
# Telling the user what we're doing, and then setting variable "target" to the open function and giving it the argument(?) filename and setting the w+ flag, which tells python it can open the file in read and write mode.
print("opening the file (and truncating it at the same time)...")
target = open(filename, 'w+')
# We don't need to 'truncate' the file because opening it with write automatically truncates it!
#print("Truncating the file. Goodbye!")
#target.truncate()
# Asking the user for input, then setting that input into variables.
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
# Telling the user what we're doing.
print("I'm going to write these to the file.")
# Using the write function on the variable "target" and specifying that we're taking the values of the variables line1, line2, and line3 and writing them to the file, and also entering a newline between them. And complying with study drill 3, we're using the + sign to concatenate the string!
target.write(line1+'\n'+line2+'\n'+line3+'\n')

# Per Study Drill 2 we're gonna read the file now and print it's new contents... STOP! Like a tape deck or something, we can't read what we've written until we tell python to go back to the beginning of the file. THEN we print the contents. Tyson says this is scary and we should flush/close it first, but YOLO
target.seek(0)
print("...and then display them for you...")
print(target.read())

# Telling the user what we're doing, and closing the variable "target"
print("Before finally closing it.")
target.close()
