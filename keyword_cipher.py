import random
import re

from cipher import Cipher

class KeywordCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.codeword = input("What codeword would you like?").lower()
        re.sub(r'[A-Za-z]+', '', self.codeword)
        diff = "".join([letter for letter in self.alphabet if letter not in self.codeword])
        self.values = self.codeword+diff
        self.spaces =  ['!', '*', '^', '(']

    def encrypt(self, message):
        """Encryption for Keyword:
        Determines the letter matching of the keyword alphabet to the plain alphabet.
        """

        encryption = {letter1:letter2 for letter1, letter2 in zip(self.values, self.values[::-1])}

        encrypted_mess = []
        for letter in message:
            if letter in encryption.keys():
                for key, value in encryption.items():
                    if key == letter:
                        encrypted_mess.append(value)
            else:
                encrypted_mess.append(random.choice(self.spaces))
        encrypted_mess = "".join(encrypted_mess)

        Cipher.block_code(self, encrypted_mess)

    def decrypt(self, message):
        """Decryption for Keyword:
        Determines the letter matching of the keyword alphabet to the plain alphabet.
        """

        encryption = {letter1:letter2 for letter1, letter2 in zip(self.values[::-1], self.values)}
        encrypted_mess = []
        for letter in message:
            if letter in encryption.keys():
                for key, value in encryption.items():
                    if key == letter:
                        encrypted_mess.append(value)
            elif letter in self.spaces:
                encrypted_mess.append(" ")
            else:
                encrypted_mess.append("")

        encrypted_mess = "".join(encrypted_mess)

        print(encrypted_mess.upper())
