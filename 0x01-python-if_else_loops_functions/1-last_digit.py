#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    lastdegit = -(abs(number % 10))
else:
    lastdegit = number % 10
if (lastdegit > 5):
    print(f"Last digit of {number} is {lastdegit} and is greater than 5")
elif (lastdegit == 0):
    print(f"Last digit of {number} is {lastdegit} and is 0")
else:
    print(f"Last digit of {number} is {lastdegit} and is less than 6 and not 0")