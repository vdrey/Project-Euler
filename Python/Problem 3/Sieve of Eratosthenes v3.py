# Sieve version 3

print('Enter your target value. (Must be greater than 500)')
TARGET = input()
TARGET = int(TARGET)

possTerm = int(TARGET/460) + 1
possList = [3]

# Def section

def factCheck(possTerm):
    if TARGET/possTerm == int(TARGET/possTerm):
        return True
    else:
        return False

def primeCheck(possTerm):

    for term in possList:

        if possList.index(term) == len(possList) - 1 and possTerm/term != int(possTerm/term):
            return True

        elif  possList.index(term) == len(possList) - 1 and possTerm/term == int(possTerm/term):
            return False

        else:
            return None

# This is using a while loop
''' 
def primeCheck(possTerm):
    b = -1
    while b < len(possList)-1: #This should check all but the last known prime
        b = b + 1

        if possTerm/possList[b] == int(possTerm/possList[b]):
            return False
        
        elif possTerm/possList[b] != int(possTerm/possList[b]):
'''

# This time, the list will be generated while checking primality and if it is a factor or not all at the same time

a = 0

while possTerm > int(TARGET/460) and possTerm < int(TARGET/450):


    if factCheck(possTerm) == True and primeCheck(possTerm) == True:
        print(possTerm)
        possList.append(possTerm)
        possTerm = possTerm + (2 * a)
        a = a + 1

    else:
        possTerm = possTerm + (2 * a)
        a = a + 1
        
