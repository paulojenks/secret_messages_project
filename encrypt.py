def encrypt(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    message = message.replace(" ", "")
    encryption = {letter1:letter2 for letter1, letter2 in zip(alphabet, alphabet[::-1])}

    em = []
    for letter in message:
        if letter in encryption.keys():
            for key, value in encryption.items():
                if key == letter:
                    em.append(value)
    em = "".join(em)
    block_code(em)

def block_code(em_2):
    block_code = []
    count = 0
    while count < len(em_2):
        block_code.append(em_2[count:count+5])
        count += 5

    print(" ".join(block_code))
    
    
encrypt("Hello")

