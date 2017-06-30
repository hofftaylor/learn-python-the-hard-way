# Exercise 8 - Printing, Printing

# Set a variable to be a string with four empty ...strings? Variables?
formatter = "{} {} {} {}"

# Print the output of the variable formatter calling the format function, and then having it fill those four empty ... things with the comma delimited values or strings.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# This one in particular sends the variable formatter to the format function. Essentially it's calling itself and then printing the string literally.
print(formatter.format(formatter, formatter, formatter, formatter))
# This line shows that you can have separate lines and unclosed parens and it will still process them side by side.
print(formatter.format(
    "Try your",
    "own text here,",
    "maybe a poem,",
    "or a bob dylan song about fear."
))
