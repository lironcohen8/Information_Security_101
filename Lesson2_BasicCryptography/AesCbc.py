# Use PyCrypto to encrypt and decrypt with AES-CBC:
# Implement a function encrypt, that given a plaintext and a  16 -byte ( 128  bit) key  k ,
# picks a random  16 -byte ( 128  bit) IV,
# and returns a ciphertext encrypted with AES-CBC with the IV prepended to the ciphertext (in bytes).
#
# You may assume that the plaintext length (in bytes) is a multiple of 16.
#
# Implement a function decrypt, that given a ciphertext (as formatted by the encrypt function)
# and a 16 -byte ( 128  bit) key  k , returns the plaintext as decrypted by AES-CBC (in 'latin1').


from Crypto.Cipher import AES
from Crypto import Random


def aes_encrypt(plaintext, k):
    IV = Random.new().read(len(k))
    cipher = AES.new(k, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(plaintext)
    return IV + ciphertext


def aes_decrypt(ciphertext, k):
    IV = ciphertext[:len(k)]
    cipher = AES.new(k, AES.MODE_CBC, IV)
    return cipher.decrypt(ciphertext).decode('latin1')

