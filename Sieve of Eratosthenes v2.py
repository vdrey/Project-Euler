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
    
print(possList)
print()
print('You must press enter to continue')
input()

# This calculates the square root of the TARGET

import math

sqrtTARGET = math.sqrt(TARGET)
sqrtTARGET = int(sqrtTARGET)


# The sieve

# a is the term in the possList
# Primes is the list of primes
# m is what a is being multiplied by

a = 1
primes = [2,3]
