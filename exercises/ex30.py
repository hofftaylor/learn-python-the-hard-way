#Exercise 30 - Else and If

people = 30
cars = 40
trucks = 15
# If cars are greater than people, print string. Otherwise continue program.
if cars > people:
    print("We should take the cars.")
# If cars are less than people, print this string. Otherwise run Else code block.
elif cars < people:
    print("We should not take the cars.")
# This is the else code block, it only runs if elif says to.
else:
    print("We can't decide.")
# If trucks are greater than cars, print string. Otherwise continue program.
if trucks > cars:
    print("That's too many trucks.")
# If trucks are less than cars, print string. Otherwise run Else code block.
elif trucks < cars:
    print("Maybe we could take the trucks.")
# This is an else code block, it only runs if the elif above says to.
else:
    print("We still can't decide.")
# If people are less than trucks, print string. Otherwise continue the program.
if people > trucks:
    print("Alright, let's just take the trucks.")
# This is an else code block, it only runs if the above statement is false.
else:
    print("Fine, let's stay home then.")

