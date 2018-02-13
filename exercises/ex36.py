# Exercise 36 - Designing and Debugging

from sys import exit


def start():
    score = 0
    print("""You walk up to the Labrinth Registration Center(tm) 
            and ask for your battle forms. Do you get them for free?""")
    action = input("RegCenter> ")
    
    if "free" or "yes" in action:
        print("""The creature at the counter croaks at you:
        "No, I'm sorry but you'll have to pay the entry fee."
        Well, it was worth a try. You slide your federation credits across the table.""")
        nextroom()  
    elif "no" in action:
        print("""No way they're free. You miss every shot you don't take. You slide your credits across the table.""")
        nextroom()
    else:
        print("""The creature at the counter mumbles incoherently at you, something is probably wrong with your translator. It alarmingly swings a device at you, deducting the credits from your account before pushing a button, screaming as spittle flies from its mouth.""")
        nextroom()

def room_0():
    print("Content")

def room_1():
    print("Content")

def room_2():
    print("Content")

def room_3():
    print("Content")

def room_4():
    print("Content")

def room_5():
    print("Content")

def room_6():
    print("Content")

def room_7():
    print("Content")

def room_8():
    print("Content")

def room_9():
    print("Content")

def nextroom():
    print("""A portal materializes in front of you with a loud pop.
            You move forward, eager to put this room behind you.""")
    score = score + 1
    print(f"Somewhere in the multiverse, a counter ticks up to {score} rooms passed!")

def scorecheck():
    if score < 10:
        nextroom()
    else:
        gameover("You are victorious, crowds cheer as you emerge from the labrynth unharmed!")

def scorecount():
    score = room_survived

def gameover(why):
    print(why, "Game Over!")
    print(f"You survived {score} rooms!")
    exit(0)

start()

