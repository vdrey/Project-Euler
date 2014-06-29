# This is to generate a list of numbers for the Sieve of Eratsthenes

print('Enter your target value. (Must be greater than 24)')
TARGET = input()
TARGET = int(TARGET)

termR1 = 23
possList = [2,3,5,7,11,13,17,19]

while termR1 < TARGET:

    a = termR1

    if a/3 == int(a/3):
        termR1 = termR1 + 2

    elif a/5 == int(a/5):
        termR1 = termR1 + 2

    elif a/7 == int(a/7):
        termR1 = termR1 + 2

    elif a/11 == int(a/11):
        termR1 = termR1 + 2

    elif a/13 == int(a/13):
        termR1 = termR1 + 2

    elif a/17 == int(a/17):
        termR1 = termR1 + 2

    elif a/19 == int(a/19):
        termR1 = termR1 + 2

    else:
        termR1 = termR1 + 2
        possList.append(a)


