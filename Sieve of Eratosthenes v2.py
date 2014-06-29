# Sieve version 2

# This generates a list of odd numbers < TARGET 

print('Enter your target value. (Must be greater than 24)')
TARGET = input()
TARGET = int(TARGET)

termR1 = 5
possList = [2,3]

while termR1 < TARGET:

    possList.append(termR1)
    termR1 = termR1 + 2
    print(possList[len(possList)-1])
    
print(len(possList))
print()
print('You must press enter to continue')
input()

'''# This calculates the square root of the TARGET

import math

sqrtTARGET = math.sqrt(TARGET)
sqrtTARGET = int(sqrtTARGET)'''


# The sieve

# a is the term in the possList
# b is the int(value) of a
# c is the term in the primes
# d is the int(value) of c
# Primes is the list of primes
# m is what a is being multiplied by

a = 2
primes = [2,3,5]


while a < len(possList):

    a = a + 1
    c = 1

    b = possList[a]
    d = primes[c]

    while c < len(primes) - 1:

        if b/d == int(b/d):
            break

        else:
            c = c + 1

    while c == len(primes) - 1:

        if b/d == int(b/d):
            break

        else:
            primes.append(d)
            break


print(primes)
            
