# Exercise 36 - Designing and Debugging

from sys import exit
import random


def score():
    points = 0


def start():
    score.points = 0
    print("""You walk up to the Labrinth Registration Center(tm)
            and ask for your battle forms. Do you get them for free?""")
    action = input("RegCenter> ")

    if "free" or "yes" in action:
        print("""The creature at the counter croaks at you:
        "No, I'm sorry but you'll have to pay the entry fee."
        Well, it was worth a try. You slide your federation credits across the
              table.""")
        nextroom()
    elif "no" in action:
        print("""No way they're free. You miss every shot you don't take. You
              slide your credits across the table.""")
        nextroom()
    else:
        print("""The creature at the counter mumbles incoherently at you,
              something is probably wrong with your translator. It alarmingly
              swings a device at you, deducting the credits from your account
              before pushing a button, screaming as spittle flies from its
              mouth.""")
        nextroom()


def rooms():
    pass


def nextroom():
    print("""A portal materializes in front of you with a loud pop.
            You move forward, eager to put this room behind you.""")
    score.points = score.points + 1
    print("""Somewhere in the multiverse, a counter ticks up to {score} rooms
          passed!""")
    availRoomRange = + nextRoomNumber
    if score.points < 10:
        nextRoomNumber = random.randint(availRoomRange)
        if nextRoomNumber == 0:
            pass
        elif nextRoomNumber == 1:
            pass
        elif nextRoomNumber == 2:
            pass
        elif nextRoomNumber == 3:
            pass
        elif nextRoomNumber == 4:
            pass
        elif nextRoomNumber == 5:
            pass
        elif nextRoomNumber == 6:
            pass
        elif nextRoomNumber == 7:
            pass
        elif nextRoomNumber == 8:
            pass
        if nextRoomNumber == 9:
            pass
    else:
        gameover("""You are victorious, crowds cheer as you emerge from the
                 labryinth unharmed!""")


def gameover(why):
    print(why, "Game Over!")
    print("""You survived {score} rooms!""")
    exit(0)


start()
