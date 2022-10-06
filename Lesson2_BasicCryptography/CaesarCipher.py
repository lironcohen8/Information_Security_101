# Implement Caesar’s cipher:
# implement a function encrypt that given a plaintext string and a key  k (how many letters to shift)
# returns a ciphertext where each character is shifted  k  places.
# You can assume all characters are lowercase letters, with no punctuation or spaces backward
# so with  k=2  'c' is encrypted by 'a'

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, k):
    cipher_text = ""
    for letter in plaintext:
        cipher_text += alphabet[(alphabet.find(letter) - k) % 26]
    return cipher_text


