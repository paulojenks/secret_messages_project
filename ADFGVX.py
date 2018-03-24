from cipher import Cipher

class Adfgvx(Cipher):
    def __init__(self):
        super().__init__()
        self.codeword = input("What codeword would you like?").lower()
        self.keyword = input("What is your keyword?").lower()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.polybius_square = self.create_polybius_square()

    def create_polybius_square(self):
        diff = "".join([letter for letter in self.alphabet if letter not in self.codeword])
        alpha_list = self.codeword+diff

        new_alphabet = [letter for letter in alpha_list]
        pb = [(one+two) for one in 'ADFGVX' for two in 'ADFGVX']
        polybius_square = {letters:alpha for letters, alpha in zip(pb, new_alphabet)}

        return polybius_square

    def encrypt(self, message):
        encrypted_message = [key for key, value in self.polybius_square.items()
                            for i in range(len(message)) if message[i] == value]
        em_1 = []
        for letter in message:
            if letter in self.polybius_square.values():
                for key, value in self.polybius_square.items():
                    if value == letter:
                        em_1.append(key)
        encrypted_message = list("".join(em_1))
        letters = sorted([(self.keyword[i],encrypted_message[i::len(self.keyword)])
                            for i in range(len(self.keyword))])
        em_2 = [letter[1] for letter in letters]
        em_2 = [item for sub_list in em_2 for item in sub_list]
        encrypted_mess = "".join(em_2)

        Cipher.block_code(self, encrypted_mess)

    def decrypt(self, message):
        sorted_keyword = sorted([letter for letter in self.keyword])
        dm = [letter for letter in message]
        dm = [()]
