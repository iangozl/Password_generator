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

# 1) Recieve user's input of how long he/she wants the password to be
# 2) Create an empty array

print(string.ascii_lowercase)

password = arr.array('u')

pwd_length = input("How many characters will your password have?:\n")


# Verification

if pwd_length.isnumeric():
    pwd_length = int(pwd_length)
    pwd_list = random.choices(string.ascii_lowercase, k = pwd_length)

    print('Your password is:',''.join(x for x in pwd_list))

else:
    print("Please enter an integer number")

