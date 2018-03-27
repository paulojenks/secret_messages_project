import random

from cipher import Cipher

class Atbash(Cipher):
    def __init__(self, **kwargs):
        super().__init__()

        for key, value in kwargs.items():
            setattr(self, key, value)


    def encrypt(self, message):
        """Encryption for Atbash:
        Maps letter in alphabet to its reverse.
        """
        encryption = {letter1:letter2 for letter1, letter2 in zip(self.alphabet, self.alphabet[::-1])}
        encrypted_mess = []
        for letter in message:
            if letter in encryption.keys():
                for key, value in encryption.items():
                    if letter == key:
                        encrypted_mess.append(value)
            else:
                encrypted_mess.append(random.choice(self.spaces))
        encrypted_mess = "".join(encrypted_mess)

        Cipher.block_code(self, encrypted_mess)

    def decrypt(self, message):
        """Decryption for Atbash:
        To return your original input, reference the letter position
        in the reversed alphabet.
        """
        encryption = {letter1:letter2 for letter1, letter2 in zip(self.alphabet[::-1], self.alphabet)}
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
