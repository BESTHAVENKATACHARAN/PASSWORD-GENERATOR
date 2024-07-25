import string
import random
def password_generator(min_len,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    characters=letters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    pwd=""
    criteria=False
    has_number=False
    has_special=False
    while not criteria or len(pwd)<min_len:
        char=random.choice(characters)
        pwd+=char
        if char in digits:
            has_number=True
        elif char in special:
            has_special=True
        criteria=True
        if numbers:
            criteria=has_number
        if special_characters:
            criteria=criteria and has_special
    return pwd

min_length=int(input('Enter minimum length of password : '))
number=input('Would you like to have numbers in your password ? (Y/y): ').lower()
special=input('Would you like to have special characters in your password ? (Y/y): ').lower()
if number=='y':
    number=True
else:
    number=False
if special=='y':
    special=True
else:
    special=False

password=password_generator(min_length,number,special)
print('Generated Password is : ',password)