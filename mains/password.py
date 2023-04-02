


"""
I created a simple password generator using Python, primarily utilizing the "string" and "random" modules.

"""


# This code imports the "Upper_Case_Letters" variable and "getting_Uppercase" function, which will generate and return a random uppercase character.
from Uppercase import Upper_Case_Letters, getting_Uppercase
# Importing the Lower_Case_Letters variable and the getting_Lowercase() function, which will return a random lowercase character.
from Lowercase import Lower_Case_Letters, getting_Lowercase
from Num import Numbers, getting_Numbers  #Basically importing the Numbers variable and the getting_Numbers function, which will generate and return a random number character.
# Basically, the code is importing the "Punctuation" variable and "getting_Pun" function, which are used to generate and return a random punctuation character.
from Puns import Punctuation, getting_Pun

import logging


"""

In this code, I am importing crucial functions and methods from other files, as well as importing the "logging" module to notify errors related to specific actions.
"""


logging.basicConfig(level=logging.WARNING)


""" 

The "passwords" function is the primary function.


"""

def passwords():
    #creating varables
    running  = True
    while running:  # A "while" loop is being created, which runs until certain conditions are met.
        try:
            how_many_passwords_you_need = int(input(
                "How many passwords do you need? (Max is 10)"))  # An "input" function is used to enable the user to enter the maximum number of passwords required, with a limit of 10.
            
            #A "for" loop is used to iterate over a list of numbers, which in this case is the input provided by the user.
            for i in range(how_many_passwords_you_need):
                if how_many_passwords_you_need > 10: 
                    # An "if" statement is included to limit the maximum number of passwords to 10 if the user enters a number greater than 10.
                    message = "The maximum allowed value is 10."
                    logging.warning(message) #giving the user warning
                    break
                # A variable is being created to display the generated password, and a string is being used to call all the functions.
                password = f"Password: {getting_Uppercase()}{getting_Lowercase()}{getting_Numbers()}{getting_Pun()}" 
                print(password) #printing the password out
                #making the while loop false so it will stop the loop
                running = False
        except ValueError:
            #If the user enters a string or leaves the input empty, a warning message is displayed.
                logging.warning("Please enter a valid integer value for the number of passwords required.")
            
            
        


if __name__ == '__main__':
    passwords() #calling the function
