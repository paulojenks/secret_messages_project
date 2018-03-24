from atbash import Atbash
from keyword_cipher import KeywordCipher
from polybius_square import PolybiusSquare

def get_messages():
    print("This is the Secret Messages Project for the Treehouse Techdegree.")
    print("These are the current available ciphers:\n")
    print("-(At)bash-")
    print("-(K)eyword-")
    print("-(P)olybius Square-")
    print("\n\n")

    cipher = input("Which cipher would you like to use?\n>>>").lower()
    choice = input("Would you like to (e)ncrypt or (d)ecrypt a message?").lower()
    message = input("What is your message?").lower()
    message = message.replace(" ", "")

    if cipher == 'atbash' or cipher == 'at':
        cipher = Atbash()
    elif cipher == 'keyword' or cipher == 'k':
        cipher = KeywordCipher()
    elif cipher == 'polybius square' or cipher == 'p':
        cipher = PolybiusSquare()
    else:
        print("Sorry, I didn't get that.  Please choose from the list again.")

    if choice == 'e':
        cipher.encrypt(message)
    else:
        cipher.decrypt(message)


get_messages()
