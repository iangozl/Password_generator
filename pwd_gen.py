"""
    Write a programme, which generates a random password for the user. Ask the user how long they 
    want their password to be, and how many letters and numbers they want in their password. 
    Have a mix of upper and lowercase letters, as well as numbers and symbols. 
    The password should be a minimum of 6 characters long.
""" 

#Don't forget about the .alph()
import string
import random
import array as arr

# List of all the allowed characters in the password


# All the variables

all_char = string.ascii_letters + string.digits + string.punctuation
pwd_length = 0

# Verification


while pwd_length < 6:

    try:
        pwd_length = int(input("How many characters will your password have?:\n"))
        if pwd_length >= 6:

            pwd_list = random.choices(all_char, k = pwd_length)

            print('Your password is:',''.join(x for x in pwd_list))
            break
    
        else:
            print('It should be greater than 6 digits!')

    except:
        print("Please enter an integer number")

