import random
import string

def generate_password(min_lengh,numbers=True,special_character=True):
    #this function takes the minimum characters, if the user wants a digit and if the user wants a special character
    #it returns a password with the criteria specified.
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_character:
        characters+=special
    
    password=""
    meets_chriteria = False
    has_number=False
    has_special=False

    while not meets_chriteria or len(password)<min_lengh:
        new_char=random.choice(characters)
        password += new_char
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special = True

        meets_chriteria=True

        if numbers:
            meets_chriteria=has_number
        if special_character:
            meets_chriteria=meets_chriteria and has_special

            

    return password
min_len = int(input("Minimum characters?:"))
include_numbers = input("Do you want to include numbers? y/n: ").lower() == 'y'
include_special = input("Do you want to include special characters? y/n: ").lower() == 'y'
prova = generate_password(min_len,include_numbers,include_special)
print(prova)