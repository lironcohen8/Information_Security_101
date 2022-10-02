# Below is code that implements an InvertedCaesar cipher: its encryption shifts letters k places forward.
# Find the plaintext and key of the following message that was encrypted using InvertedCaesar
# kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)


def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)


def brute_force(ciphertext):
    for k in range(0, 26):
        plain_text = decrypt(ciphertext, k)
        print(plain_text, k)


brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")