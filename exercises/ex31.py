#Exercise 31 - Making Decisions

print('''You enter a dark room with two doors.
Do you go through door #1 or door #2?''')

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss of Cthulu's retina.")
    print("1. Blueberries.")
    print("2. A human skin hung to dry by clothespins.")
    print("3. Yellow revolvers scream melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives, powered by a mind of jello.")
        print("Good Job!")
    elif insanity == "3":
        print("The revolvers fire madly, their songs penetrate your skull, killing you instantly.")
        print("Good Job!")
    else:
        print(f"You try doing {insanity}, but Cthulu cares little for the struggles of mortal beings. You are subsumed whole into the abyss. Good Job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")

