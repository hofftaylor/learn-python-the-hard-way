# Exercise 36 - Designing and Debugging

from sys import exit
import random


def start():
    score.points = 0
    print("""You walk up to the Labrinth Registration Center(tm)
and ask for your battle forms. Do you get them for free?""")
    action = input("RegCenter> ")
    if action == "yes":
        # Can't seem to use an or statement here w/o breaking logic?
        print("""The creature at the counter croaks at you:
"I'm sorry but you'll have to pay the entry fee."
Well, it was worth a try. You slide your federation credits across the
table.""")
        nextroom()
    elif action == "no":
        print("""No way they're free. You miss every shot you don't take. You
slide your credits across the table.""")
        nextroom()
    else:
        print("""The creature at the counter mumbles incoherently at you,
something is probably wrong with your translator. It alarmingly
swings a device at you, deducting the credits from your account
before pushing a button, screaming strange alien syllables as spittle flies
from its mouth.""")
        gameover("""You're dropped into a pool of sulfur, must've told them the
wrong thing...""")


def score():
    pass


def rooms():
    pass


def nextroom():
    print("""A portal materializes in front of you with a loud pop.
You move forward, eager to put this room behind you.""")
    score.points += 1
    print(f"""Somewhere in the multiverse, a counter ticks up to {score.points} rooms
passed!""")
    if score.points <= 10:
        nextRoomNumber = random.randint(0, 9)
        if nextRoomNumber == 0:
            print("Room 0")
            pass
        elif nextRoomNumber == 1:
            print("Room 1")
            pass
        elif nextRoomNumber == 2:
            print("Room 2")
            pass
        elif nextRoomNumber == 3:
            print("Room 3")
            pass
        elif nextRoomNumber == 4:
            print("Room 4")
            pass
        elif nextRoomNumber == 5:
            print("Room 5")
            pass
        elif nextRoomNumber == 6:
            print("Room 6")
            pass
        elif nextRoomNumber == 7:
            print("Room 7")
            pass
        elif nextRoomNumber == 8:
            print("Room 8")
            pass
        elif nextRoomNumber == 9:
            print("Room 9")
            pass
        else:
            pass
    else:
        gameover("""You are victorious, crowds cheer as you emerge from the
labryinth unharmed!""")


def gameover(why):
    print(why, "Game Over!")
    print(f"You survived {score.points} rooms!")
    exit(0)


start()
