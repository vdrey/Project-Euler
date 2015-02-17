# This is for Project Euler problem 3

import random

rawList = list(range(100, 1320552575)




# This removes evens (except for 2)

a = 0
noEven = []

while a < len(rawList):

    if (rawList[a])/2 == int((rawList[a])/2):
        a = a + 1

    else:
        noEven.append(rawList[a])
        a = a + 1

print("Evens Removed.")
print()
print()

# This removes multiples of single-digit primes ( 3, 5, 7)

b = 0
noSingleMults = []

while b < len(noEven):

    if noEven[b] == (3, 5, 7):
        noSingleMults.append(noEven[b])
        b = b + 1

    elif (noEven[b])/3 == int((noEven[b])/3):
        b = b + 1
        

    elif (noEven[b])/5 == int((noEven[b])/5):
        b = b + 1
        

    elif (noEven[b])/7 == int((noEven[b])/7):
        b = b + 1
        

    else:
        noSingleMults.append(noEven[b])
        b = b + 1


print("single mults removed")
