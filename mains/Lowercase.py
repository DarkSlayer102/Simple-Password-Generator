import string
import random


"Importing the modules "


# A variable is being created to store all the lowercase characters.
Lower_Case_Letters = string.ascii_lowercase


""" This function generates a random lowercase character and returns it."""
def getting_Lowercase():
    newLowercase = []
    for i in Lower_Case_Letters:
        newLowercase.append(i)
    random_Lower = random.choice(newLowercase)
    return random_Lower

