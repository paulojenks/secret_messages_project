from cipher import Cipher

class PolybiusSquare(Cipher):
    def __init__(self):
        super().__init__()
        self.codeword = input("What codeword would you like?").lower()
        self.polybius_square = self.create_polybius_square()

    def create_polybius_square(self):
        """Creates the Polybius Square for
        either encryption or decryption
        """
        diff = "".join([letter for letter in self.alphabet
                        if letter not in self.codeword])
        alpha_list = self.codeword+diff

        new_alphabet = [letter for letter in alpha_list]
        pb = [(str(one)+str(two)) for one in range(1,7) for two in range(1,7)]
        polybius_square = {letters:alpha for letters, alpha
                            in zip(pb, new_alphabet)}

        return polybius_square

    def encrypt(self, message):
        """Encryption for Polybius Square:
        Uses Polybius Square plus a keyword for extra security to match
        the letters in the message with the Polybius Square
        """
        em = []
        for letter in message:
            if letter in self.polybius_square.values():
                for key, value in self.polybius_square.items():
                    if value == letter:
                        em.append(key)
        encrypted_mess = "".join([num for sub_list in em for num in sub_list])

        Cipher.block_code(self, encrypted_mess)

    def decrypt(self, message):
        """Decryption for Polybius Square:
        Uses Polybius Square plus a keyword for extra security to match
        the letters in the message with the Polybius Square
        """
        em = [message[i:i+2] for i in range(0,len(message), 2)]
        encrypted_mess = []
        for num in em:
            if num in self.polybius_square.keys():
                for key, value in self.polybius_square.items():
                    if key == num:
                        encrypted_mess.append(value)
        encrypted_mess = "".join(encrypted_mess)
        Cipher.block_code(self, encrypted_mess)
