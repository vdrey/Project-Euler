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


# This calculates the square root of the TARGET

import math

sqrtTARGET = math.sqrt(TARGET)
sqrtTARGET = int(sqrtTARGET)

# Now for the sieve

factor = 0

while possList[factor] < sqrtTARGET:

    multiple = 2

    if (possList[factor] * multiple)/2 == int((possList[factor] * multiple)/2): #optomize to remove this block
        possList.remove(possList[factor] * multiple)
        factor = factor + 1

    elif possList[factor] * multiple < TARGET:
        possList.remove(possList[factor] * multiple)
        factor = factor + 1

    else:
        break

print(possList)

    
