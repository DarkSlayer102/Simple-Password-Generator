import string
import random

"Importing the modules "


# A variable is being created to store all the specific characters.
Punctuation = string.punctuation

""" This function generates a random punctuation character and returns it."""

def getting_Pun():
    newPun = []
    for i in Punctuation:
        newPun.append(i)
    random_Pun = random.choice(newPun)
    return random_Pun
