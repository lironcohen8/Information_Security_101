# Brute force a message encrypted with AES-CBC,
# given that it was encrypted with a key that represents a phone number of someone from Tel-Aviv,
# padded with zeroes (in other words, 9 digits, beginning with 036, and with trailing '0' to a length of 16 bytes,
# like this: 036######0000000).
#
# You should test your brute-force cracker code using the outputs from your encrypt function of Hackxercise 6.


from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english


def brute_force_aes(ciphertext):
    plaintext = "0" # dummy for initialization
    key_center = 000000
    while not is_english(plaintext):
        k = "036" + str(key_center).rjust(6) + "0000000"
        plaintext = aes_decrypt(ciphertext, k)
        key_center += 1
    return plaintext,k
