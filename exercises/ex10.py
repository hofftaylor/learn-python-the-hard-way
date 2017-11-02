# Exercise 10 - What was that?!

# Using the \t to create a tabbed string.
tabby_cat = "\t I'm tabbed in."
# Using the \n to split a string onto a new line.
persian_cat = "I'm split \non a line."
# Using the basckslash escape character to 'escape' the system using it as an escape character, so I can print just one backslash character.
backslash_cat = "I'm \\ a \\ cat."

# Using the triple-quotes to create a freeform string. We use a \t to create new tabs for our list and \n to make a new line for one of the bullet points that's contained in the same line.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# I'm doing the same thing here as I did on ex8, to satisfy drill 3 here, but I'm still unclear as to why or what the curly brackets are for...?
drill3_cat = "{}"

# Printing all the variables and their contents, as well as using the formatted string lesson from ex8 to satisfy drill 3.
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(drill3_cat.format('I\'m a cat that satisfies the requirements for drill 3, \f (also I have zero imagination.)'))
