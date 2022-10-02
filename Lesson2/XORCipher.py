# Write a XOR cipher:
# implement a function encrypt that given a plaintext string and a key \(k\) (also a string),
# returns a ciphertext where each character is XORed with its respective character in \(k\).
# Assume that the plaintext and key have the same length. (that is, plaintext[i] is XORed with k[i]).

def encrypt(plaintext, k):
    result = []
    for i, v in enumerate(plaintext):
        result.append(chr(ord(v) ^ ord(k[i])))
    return ''.join(result)