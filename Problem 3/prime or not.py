# This program determines if a number is prime or not

import random
import time

print('press enter')
#input()


# This is to generate a list of numbers

rawList = []
rolls = 0

while rolls < 1000:

    rolls = rolls + 1
    n = random.randint(2, 50)
    rawList.append(n)

print(rawList)
print()



# This removes evens (except for 2)

a = 0
noEven = []

while a < len(rawList):

    if rawList[a] == 2:
        noEven.append(rawList[n])
        a = a + 1

    elif (rawList[a])/2 == int((rawList[a])/2):
        a = a + 1

    else:
        noEven.append(rawList[a])
        a = a + 1

print(noEven)
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


print(noSingleMults)






