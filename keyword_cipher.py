from cipher import Cipher

class KeywordCipher(Cipher):
    def __init__(self):
        super().__init__()
        self.codeword = input("What codeword would you like?").lower()

    def encrypt(self, message):
        """Encryption for Keyword:
        Determines the letter matching of the keyword alphabet to the plain alphabet.
        """
        diff = "".join([letter for letter in self.alphabet if letter not in self.codeword])
        values = self.codeword+diff

        encryption = {letter1:letter2 for letter1, letter2 in zip(values, values[::-1])}

        encrypted_mess = []
        for letter in message:
            if letter in encryption.keys():
                for key, value in encryption.items():
                    if key == letter:
                        encrypted_mess.append(value)
        encrypted_mess = "".join(encrypted_mess)

        Cipher.block_code(self, encrypted_mess)

    def decrypt(self):
        """Decryption for Keyword:
        Determines the letter matching of the keyword alphabet to the plain alphabet.
        """
        diff = "".join([letter for letter in self.alphabet if letter not in self.codeword])
        values = self.codeword+diff

        encryption = {letter1:letter2 for letter1, letter2 in zip(values[::-1], values)}
        encrypted_mess = []
        for letter in message:
            if letter in encryption.keys():
                for key, value in encryption.items():
                    if key == letter:
                        encrypted_mess.append(value)
        encrypted_mess = "".join(encrypted_mess)

        Cipher.block_code(self, encrypted_mess)
