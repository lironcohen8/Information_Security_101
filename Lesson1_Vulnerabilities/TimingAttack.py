# The function check_password(password) is used by a safe with 4-digits passwords, and is susceptible to timing attacks.
# More specifically, it takes it around 0.1 seconds to check one digit –
# so brute-forcing all the possible combinations will take more than an hour.
# Can you implement a way to crack its password in less than a minute?
import time
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.pswd import real_password

def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    guess = "0000" # Four-digit password
    guess_is_correct = False
    index_to_check = 0
    while True:
        start_time = time.time()
        guess_is_correct = check_password(guess)
        end_time = time.time()
        diff_time = round(end_time - start_time, 1)
        if guess_is_correct:
            break
        index_to_check = round(diff_time / 0.1) - 1
        guess = str(int(guess) + pow(10, 4 - index_to_check - 1))
    return guess

print(crack_password())

