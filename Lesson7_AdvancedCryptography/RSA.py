# A real RSA system:
# Use pycrypto to encrypt and decrypt a message using RSA.

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt(m, public_key):
    cipher_rsa = PKCS1_OAEP.new(public_key)
    return cipher_rsa.encrypt(m).decode(), key

def decrypt(c, private_key):
    cipher_rsa = PKCS1_OAEP.new(private_key)
    return cipher_rsa.decrypt(c).decode()

def sign(m, private_key):
    cipher_rsa = PKCS1_OAEP.new(private_key)
    return cipher_rsa.decrypt(m).decode()

def verify(m, s, public_key):
    cipher_rsa = PKCS1_OAEP.new(public_key)
    return m == cipher_rsa.encrypt(s).decode(), key