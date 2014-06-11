# Sieve version 2

# This generates a list of odd numbers < TARGET 

print('Enter your target value. (Must be greater than 24)')
TARGET = input()
TARGET = int(TARGET)

termR1 = 5
possList = [2,3]

while termR1 < TARGET:

    a = termR1
    termR1 = termR1 + 2
    possList.append(a)

print(possList)
print()
print('You must press enter to continue')
input()
