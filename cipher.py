import random
import string
import math

class Cipher:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.spaces =  ['!', '*', '^', '(']

    def encrypt(self, message):
        raise NotImplementedError()

    def decrypt(self, message):
        raise NotImplementedError()

    def block_code(self, encrypted_mess):
        """block_code returns encrypted or decrypted Messages as blocks
        of 5 with padding
        """
        self.encrypted_mess = encrypted_mess
        if len(encrypted_mess) % 5 != 0:
            chars = ['#', '$', '&', ')']
            padding = random.choices(chars,
                                    k=math.floor(len(encrypted_mess)/5 + 1)
                                    * 5 - len(encrypted_mess))
            padding = "".join(padding)
        else:
            padding = ""
        encrypted_mess += padding
        block_code = [encrypted_mess[i:i+5] for i in
                        range(0,len(encrypted_mess), 5)]
        print(" ".join(block_code).upper())

    def unblock_code(self, message):
        """Removes padding and blocking from secret message"""
        for letter in message:
            if letter not in self.alphabet:
                message.replace(letter, " ")

        return message
