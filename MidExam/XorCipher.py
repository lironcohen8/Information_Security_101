# Eve has managed to intercept the following messages, encrypted by Alice using a XOR cipher.
# Eve suspects Alice has been using the same key to encrypt all three messages; moreover, she suspects that the third message ( m3 ) also happens to be  m1  XOR  m2 .
# Can you find the key and decipher the messages?

c1 = int('00100111010', 2)
c2 = int('01001110110', 2)
c3 = int('11010110101', 2)

# m1 ^ k = c1 => c1 ^ k = m1
# m2 ^ k = c2 => c2 ^ k = m2
# m3 ^ k = c3 => c3 ^ k = m3
# m1 ^ m2 = m3 => c1 ^ k ^ c2 ^ k = c3 ^ k => c1 ^ c2 = c3 ^ k => c1 ^ c2 ^ c3 = k

k = c1 ^ c2 ^ c3
print(bin(k))
print(bin(c1 ^ k))
print(bin(c2 ^ k))
print(bin(c3 ^ k))
