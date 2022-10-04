# Implement heuristic plaintext detection using frequency analysis:
#
# Implement a function is_english that:

# Receives a string
# Makes sure it consists of only ASCII characters (using the provided is_ascii() function)
# Counts the 3 most frequent letters in it
# Makes sure they're one of the 6 most frequent letters in English (e, t, a, o, i, n)

from collections import Counter

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    if is_ascii(s):
        s = s.lower()
        s = s.replace(' ','')
        counter = Counter(s)
        top_three = [entry[0] for entry in counter.most_common(3)]
        english_most_freq = ['e', 't', 'a', 'o', 'i', 'n']
        return all(candidate in english_most_freq for candidate in top_three)
