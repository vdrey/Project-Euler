# This is to solve proj. Euler #9

# THIS WORKS.

import sys

def checkNum(a, b, c):
    # This: (a + b) > c
    # and
    # This: (a**2)+(b**2)=(c**2)
    # must be true.
    if (a + b) <= c:
        return False
    elif (a**2) + (b**2) != (c**2):
        return False
    else:
        return True

for a in range(1000): # A
    for b in range(1000): # B
        for c in range(1000): # C
            if (a + b + c) > 1000:
                continue
            if checkNum(a, b, c):
                print()
                print(a)
                print(b)
                print(c)
                print()
                print(a*b*c)
                if (a + b + c) == 1000:
                    sys.exit('The answer')
                
