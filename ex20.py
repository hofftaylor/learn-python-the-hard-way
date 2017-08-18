# Exercise 20 - Functions and Files
# Importing argv from sys library to allow it to ask for variables on the command line
from sys import argv
# Giving argv the names of the variables it's supposed to be making
script, input_file = argv
# Defining function "print_all" as printing the contents of the file provided to argv.
def print_all(f):
    print(f.read())
# Defining function "rewind" as as seeking byte 0 of the contents of the file provided to argv.
def rewind(f):
    f.seek(0)
# Defining function "print_a_line" as printing the current line number, and then reading the line it's on in the file provided to argv.
def print_a_line(line_count, f):
    print(line_count, f.readline())
# Setting variable "current_file" to open the input_file variable provided to argv.
current_file = open(input_file)
# Printing text and giving it a new line.
print("First let's print the whole file:\n")
# Calling the function "print_all" and giving it variable current_file to chew on.
print_all(current_file)
# Printing text string to user.
print("Now let's rewind, kind of like a tape.")
# Calling the function "rewind" on variable current_file
rewind(current_file)
# Printing text string to user.
print("Let's print three lines:")
# Setting variable "current_line" to value of 1.
current_line = 1
# Calling function "print_a_line" and giving it the value of the current line and current file.
print_a_line(current_line, current_file)
# Incrementing variable "current_line"'s value by 1 and then repeating twice more.
current_line = current_line + 1
print_a_line(current_line, current_file)
# making this more efficent by using a logic contraction where += lets line 35 work the same as line 32.
current_line += 1
print_a_line(current_line, current_file)
