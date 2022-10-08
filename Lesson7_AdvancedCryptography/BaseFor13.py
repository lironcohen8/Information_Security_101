# What would be good bases for the prime 13?
# You are welcome to use the following codeboard to write a program to do the calculations for you.

p = 13
arr = []
for g in range(2, 20):
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,p-1):
        res = (g ** i) % p
        arr[res] = res
    print("g=" + str(g) + " arr=" + str(arr))