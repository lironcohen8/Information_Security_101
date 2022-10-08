# Implement the function weak-HMAC, which receives message and a  8 -bytes ( 64 -bit) long key,
# and returns its HMAC using SHA-1 with the given  8 -byte ( 64 -bit) ipad and opad.

from hashlib import sha1

ipad = b'123455678'
opad = b'abcdefghi'


def weak_hmac(m, k, ipad, opad):
    MD_tag = sha1(xor(k, ipad) + m).digest()
    MD = sha1(xor(k, opad) + MD_tag).digest()
    return MD


def bchr(i):
    return bytes([i])


def xor(s1,s2):
    return b''.join(bchr(i ^ j) for i, j in zip(s1, s2))