# Exercise 36 - Designing and Debugging

from sys import exit
import random

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
    availRoomRange =+ nextRoomNumber
    if score < 10:
        nextRoomNumber = random.randint(availRoomRange)
        if nextRoomNumber = 0:
            room_0()
        elif nextRoomNumber = 1:
            room_1()
        elif nextRoomNumber = 2:
            room_2()
        elif nextRoomNumber = 3:
            room_3()
        elif nextRoomNumber = 4:
            room_4()
        elif nextRoomNumber = 5:
            room_5()
        elif nextRoomNumber = 6:
            room_6()
        elif nextRoomNumber = 7:
            room_7()
        elif nextRoomNumber = 8:
            room_8()
        else nextRoomNumber = 9:
            room_9()
    else:
        gameover("You are victorious, crowds cheer as you emerge from the labryinth unharmed!")

def gameover(why):
    print(why, "Game Over!")
    print(f"You survived {score} rooms!")
    exit(0)

start()

