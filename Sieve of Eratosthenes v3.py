# Sieve version 3

print('Enter your target value. (Must be greater than 20)')
TARGET = input()
TARGET = int(TARGET)

possTerm = 5
possList = [3]

# Def section

def factCheck(possTerm):
    if TARGET/possTerm == int(TARGET/possTerm):
        return True
    else:
        return False

def primeCheck(possTerm):
    b = -1
    while b < len(possList)-1: #This should check all but the last known prime
        b = b + 1

        if possTerm/possList[b] == int(possTerm/possList[b]):
            return False
        
        elif possTerm/possList[b] != int(possTerm/possList[b]):

# This time, the list will be generated while checking primality and if it is a factor or not all at the same time

a = 0

while possTerm < Target:


    if factCheck(possTerm) == True and primeCheck == True:
        print(possTerm)
        possTerm = possTerm + (2 * a)
        a = a + 1

    else:
        possTerm = possTerm + (2 * a)
        a = a + 1
        
