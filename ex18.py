# Exercise 18 - Names, Variables, Code, Functions
# this one is just like your scripts with argv
# We're defining a function by a name "print_two", and then telling python that the following args are to be treated as a list. Then we print a formatted string.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# Same as above, but instead we're directly using the args instead of making them into a list?
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
# Same as above but with only one argument, just to prove we can use any number.
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
# Same as above, but with no arguments, to prove that we can do it there too.
def print_none():
    print("I got nothin'.")

print_two("Taylor","Hoff")
print_two_again("Taylor","Hoff")
print_one("First!")
print_none()
