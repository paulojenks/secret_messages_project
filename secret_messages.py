import os

from atbash import Atbash
from keyword_cipher import KeywordCipher
from polybius_square import PolybiusSquare


def clear_screen():
    """
    Clears the screen for a clean menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_messages():
    cipher = ""
    print("This is the Secret Messages Project for the Treehouse Techdegree.")
    user_prompt = "These are the current available ciphers:\n"
    user_prompt += "-(At)bash-\n"
    user_prompt += "-(K)eyword-\n"
    user_prompt += "-(P)olybius Square-\n"
    user_prompt += "-(Q)uit\n"


    while cipher not in ['at', 'k', 'p', 'q']:
        print(user_prompt)
        cipher = input("Which cipher would you like to use?\n>>>").lower()
        clear_screen()
        if cipher ==  'at':
            cipher = Atbash()
        elif cipher ==  'k':
            cipher = KeywordCipher()
        elif cipher == 'p':
            cipher = PolybiusSquare()
        elif cipher == 'q':
            break
        else:
            print("Sorry, I didn't get that.  Please choose from the list again.")
            print(user_prompt)

        message = input("What is your message?").lower()
        message = message.replace(" ", "")

        choice = input("Would you like to (e)ncrypt or (d)ecrypt the message?").lower()
        if choice == 'e':
            cipher.encrypt(message)
        else:
            cipher.decrypt(message)

if __name__ == "__main__":
    get_messages()
