"""We need two modules, random and string"""

import random
import string

# Function that takes in one mandatory, and two optional parameters.

def password_generator(length, numbers=True, special_char=True):
    pass
# naming the variables needed with the string module
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    PWD = ""
    meet_cre = False
    has_num = False
    has_spec = False

    while not meet_cre or len(PWD) < length:
        new_cha = random.choice(characters)
        PWD += new_cha

        if new_cha in digits:
            has_num = True
        elif new_cha in special:
            has_spec = True

        meet_cre = True
        if numbers:
            meet_cre = has_num
        if special_char:
            meet_cre = meet_cre and has_spec

    return PWD


len_pwd = int(input("Enter the minimum length: "))
user_n = input("Do you want numbers (y/n): ").lower() == "y"
user_s = input("Do you want special characters (y/n): ").lower() == "y"

result = password_generator(len_pwd, user_n, user_s)
print(f"Here is your generated password: {result}")
