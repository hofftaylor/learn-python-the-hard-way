# Exercise 3-1
# This script is to calculate the factorial of 64, for the age old problem "How many grains of rice per square on a chess board..."
# First we have to import the math tools.
import math
# Then we calculate the factorial of 64.
print("The factorial of 64 is...")
print(math.factorial(64))
# Wait! You're wrong! (You're right about the factorial, but...) The answer to the chessboard problem is 2^64 - 1 ! You dunce!
print("The answer to the chessboard problem is...")
print(math.pow(2,64) - 1)
# Are those the same? Let's compare them.
print("Are they the same?")
print(math.factorial(64) == (math.pow(2,64) -1))
# Of course they aren't. But we're just playing with python, so good job.
