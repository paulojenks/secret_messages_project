- Provide a command line menu providing an option to either encrypt or decrypt a
value and then a sub menu with a list of implemented ciphers.

- Write a separate class, which inherits from cipher, and implements encrypt
and decrypt functionality for each of your chosen ciphers.

- Prompt the user for input to encrypt or decrypt and, if applicable, any 0
additional input settings required to perform the cipher process.

- The input value is correctly encrypted or decrypted using the chosen cipher
and the output is displayed on the screen.

- Remember to include informative docstrings in your functions and/or methods.

- Make sure to follow the PEP 8 guidelines for coding style and write organized,
easy to follow code. General code comments are great to add to your code too.

- Implement a one time pad to secure the cipher. A one time pad is an additional
input step required prior to encrypting and decrypting a message. As long as both
the sender and receiver use the same pad, the message itself becomes secure.
Without the pad, the message cannot be recovered.

- Encrypted output is displayed in 5 character blocks, with padding added as
required. For example if the message to encrypt is “The quick brown fox.” The
output would be represented as something like “LFDKA NMYML K1KZE &XPQR”.
