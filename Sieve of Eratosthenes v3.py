# Sieve version 3

print('Enter your target value. (Must be greater than 20)')
TARGET = input()
TARGET = int(TARGET)
possTerm = 3

# Def section

def factCheck(possTerm):
    if Target/possTerm == int(Target/possTerm):
        return True
    else:
        return False

# This time, the list will be generated while checking primality and if it is a factor or not all at the same time


primeFactors = []
a = 0

while possTerm < Target:

    possTerm = possTerm + (2 * a)
    a = a + 1

    if factCheck(possTerm) == True:
        
