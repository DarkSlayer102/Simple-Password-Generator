
import string

import random

"Importing the modules "

# A variable is being created to store all the uppercasecase characters.
Upper_Case_Letters = string.ascii_uppercase


""" This function generates a random uppercase character and returns it."""
def getting_Uppercase():
    newUppercase = []
    for i in Upper_Case_Letters:
        newUppercase.append(i)
    random_Upper = random.choice(newUppercase)
    return random_Upper
