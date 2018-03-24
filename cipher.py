import random
import string
import math

class Cipher:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self, message):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def block_code(self, encrypted_mess):
        """Block_code gives user choice of returning encrypted or decrypted
        Messages as blocks of 5 with padding if necessary or returning the
        message as a single block
        """
        self.block = input("Would you like your message block coded? Y/n >>").lower()

        self.encrypted_mess = encrypted_mess
        if self.block != 'n':
            if len(encrypted_mess) % 5 != 0:
                padding = random.choices(string.ascii_uppercase,
                                        k=math.floor(len(encrypted_mess)/5 + 1)
                                        * 5 - len(encrypted_mess))
                padding = "".join(padding)
            else:
                padding = ""
            encrypted_mess += padding
            block_code = [encrypted_mess[i:i+5] for i in
                            range(0,len(encrypted_mess), 5)]
            print(" ".join(block_code).upper())
        else:
            print(self.encrypted_mess.upper())
