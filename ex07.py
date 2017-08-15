# Exercise 7 - More Printing!

#This line prints a string.
print("Mary had a little lamb.")
#This line prints a string with an empty variable and fills it with the formatted string.
print("And it's fleece was as white as {}.".format('snow'))
#This line prints another string.
print("And everywhere that Mary went.")
#This line prints the string . ten times.
print("." * 10) # What'd that do?

# These twelve lines set variables as various strings comprised of single letters
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch that comma at the end. Try removing it and see what happens.
# Removing the comma causes a syntax error.

#This line prints the variables and appends them, while including a space and then printing the content of the next strings. What I don't get is what the variable end is doing, it was never previously defined...
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
