# This is the Sieve of Eratsthenes

# This generates a list of odd numbers < TARGET 

print('Enter your target value. (Must be greater than 24)')
TARGET = input()
TARGET = int(TARGET)

termR1 = 23
possList = [2,3,5,7,11,13,17,19]

while termR1 < TARGET:

    a = termR1
    termR1 = termR1 + 2
    possList.append(a)

print(possList)
print()
print('You must press enter to continue')
input()

# This calculates the square root of the TARGET

import math

sqrtTARGET = math.sqrt(TARGET)
sqrtTARGET = int(sqrtTARGET)

# Now for the sieve

factor = 0
multiple = 3

while possList[factor] < sqrtTARGET:

    
    if possList[factor] * multiple < TARGET:
        possList.remove(possList[factor] * multiple)
        multiple = multiple + 1
        factor = factor + 1

    else:
        multiple = 3
        factor = 0
        break

print(possList)

    
