import string
import random


"Importing the modules "


# A variable is being created to store all the numbers.
Numbers = string.digits


""" This function generates a random number character and returns it."""

def getting_Numbers():
    newNumbers = []
    for i in Numbers:
        newNumbers.append(i)
    random_Number = random.choice(newNumbers)
    return random_Number
