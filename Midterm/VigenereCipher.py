# The Vigenère cipher is a method of encryption using a series of interwoven Caesar ciphers.
# It takes a codeword for a key – for example, "LEMON". Then, given a plaintext, such as "ATTACKATDAWN",
# it repeats the codeword until it matches the length of the plaintext:
#
# L	E	M	O	N	L	E	M	O	N	L	E
# A	T	T	A	C	K	A	T	D	A	W	N
# Finally, it encrypts every letter using a Caesar cipher shifted to the corresponding letter of the codeword.
#
# So, for example:
# The first "A" is encrypted using a Caesar cipher of A → L (+11), so it becomes L.
# The first "T" is encrypted using a Caesar cipher of A → E (+4), so it becomes X.
# The second "T" is encrypted using a Caesar cipher of A → M (+12), so it becomes F.
# Subsequently, we get: LXFOPVEFRNHR
#
# Implement a function, vigener_encrypt(plaintext, codeword), which takes a plaintext and codeword
# (both in uppercase letters only), and returns the vigenere-encrypted ciphertext.

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenere_encrypt(plaintext, codeword):
    code_index_to_ab_indexes = {i: alphabet.index(v) for i, v in enumerate(codeword)}
    # code_repeat = [codeword[index % len(codeword)] for index in len(plaintext)]
    result = ""
    for i, v in enumerate (plaintext):
        code_index = i % len(codeword)
        shift = code_index_to_ab_indexes[code_index]
        result += alphabet[(alphabet.index(v) + shift) % len(alphabet)]
    return result
