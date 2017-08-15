# Exercise 6 - Strings and Text
# Setting variables and printing strings!

# This line sets the variable types_of_people to the value 10
types_of_people = 10
# This line sets the variable x to the formatted string "There are {types_of_people} types of people."
x = f"There are {types_of_people} types of people."

#These two lines set variables to strings.
binary = "binary"
do_not = "don't"
# This line sets the variable y to a formatted string.
y = f"Those who know {binary}, and those who {do_not}."

# These two lines print the variables x and y.
print(x)
print(y)

# These two lines print their respective strings, as well as the varibles x and y (which are also strings...)
print(f"I said: {x}")
print(f"I also said: '{y}'")

# This line sets the variable hilarious to false
hilarous = False
# This line sets the variable joke_evaluation to a string that contains an empty (undefined?) variable
joke_evaluation = "Isn't that joke so funny?! {}"

# This line prints the variable joke_evaluation in a formatted string and (inserts?) the variable hilarious into the empty variable {}
print(joke_evaluation.format(hilarous))

# These two variables are set to strings
w = "This is the left side of..."
e = "a string with a right side."

# This prints the contents of these two variables and appends them together? With logic, I guess?
print(w + e)
