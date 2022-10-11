# Alice and Bob want to safely exchange secret messages. To do this, they need to:
#
# Agree on a symmetric key and establish a secure communication channel by running a Diffie-Hellman key exchange procedure
# Use the established symmetric key to encrypt messages to each other using a block cipher
# Your task is to help them out by implementing the SecureChannel class.
# The SecureChannel class:
#
# Receives p and g , and randomizes an a. Note that when Bob uses this function, the parameter a is really his b
# Its publish() function returns  ga(mod p)  - this output is what Alice sends to Bob; Bob uses the same function
# (except that he gets a different value)
# Its encrypt() function receives  gb(mod p)  and some text, computes the shared secret S, and encrypts the text.
# It converts the shared secret S into an encryption key for AES128 by casting it to a string of bytes,
# hashing it with SHA256, and using the first 16 bytes of the digest as the key. It then picks a random IV of 16 bytes,
# and uses PyCrypto's AES128 in CBC mode to encrypt the text. For simplicity's sake, the plaintext is always exactly 16
# characters long. The encrypt() function returns the IV prepended to the encrypted message.


import random
import hashlib
import os
from Crypto.Cipher import AES
from Crypto import Random

# you can use the imports, and you can solve with your own imports

p = 283
g = 47


class SecureChannel:

    def __init__(self, p, g):
        self.a = random.randint(1, p)

    def publish(self):
        return (g ** self.a) % p

    def encrypt(self, gb, text):
        S = ((gb ** self.a) % p).to_bytes(16, 'big')
        k = hashlib.sha256(S).digest()[:16]
        IV = Random.new().read(16)
        cipher = AES.new(k, AES.MODE_CBC, IV)
        ciphertext = cipher.encrypt(text)
        return IV + ciphertext






