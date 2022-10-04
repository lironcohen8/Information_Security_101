# Use codeboard and the standard library hashlib module to compute the MD5, SHA1
# and SHA256 (that's SHA2 with a hash size of  n=256 ) of the string "Hello, world!".

import hashlib

string_to_hash = b"Hello, world!"

md5_hash = hashlib.md5(string_to_hash)
print(md5_hash.hexdigest())

sha1_hash = hashlib.sha1(string_to_hash)
print(sha1_hash.hexdigest())

sha256_hash = hashlib.sha256(string_to_hash)
print(sha256_hash.hexdigest())