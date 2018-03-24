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
        em = []
        for letter in message:
            if letter in encryption.keys():
                for key, value in encryption.items():
                    if letter == key:
                        em.append(value)
        encrypted_mess = "".join(em)

        Cipher.block_code(self, encrypted_mess)

    def decrypt(self, message):
        """Decryption for Atbash:
        To return your original input, reference the letter position
        in the reversed alphabet.
        """
        encryption = {letter1:letter2 for letter1, letter2 in zip(self.alphabet[::-1], self.alphabet)}

        em = []
        for letter in message:
            if letter in encryption.keys():
                for key, value in encryption.items():
                    if letter == key:
                        em.append(value)
        encrypted_mess = "".join(em)

        Cipher.block_code(self, encrypted_mess)
