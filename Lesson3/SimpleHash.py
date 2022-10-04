# Implement a hash function simple_hash that given a string s, computes its hash as follows: it starts with r = 7,
# and for every character in the string, multiplies r by 31, adds that character to r, and keeps everything modulo 216.
import itertools
import string


def simple_hash(s):
    r = 7
    for char in s:
        r = (r * 31 + ord(char)) % pow(2, 16)
    return r

# Brute-force the hash function you've just written!
# Implement a function crack that given a string s, loops until it finds a different string that collides with it,
# and returns the different string.


def crack(s):
    desired_hash = simple_hash(s)
    candidate_len = 1
    while True:
        for candidate in itertools.product(string.ascii_lowercase, repeat=candidate_len):
            candidate = ''.join(candidate)
            if candidate != s and simple_hash(candidate) == desired_hash:
                return candidate
        candidate_len += 1
