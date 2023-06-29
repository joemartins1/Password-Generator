# Password Generator
# Python Projet by Joe

import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890,?;.:/!%$*+-=_-&@#"

# Password Generator Function
def password_generator(len):
    characters.strip()
    #print(list(characters.strip()))
    password_split = random.sample(characters, len)
    password = ''.join(password_split)
    print("pass:")
    print(password)

# Main Menu Function
choice = int(input("Enter a number of characters: "))
password_generator(choice)