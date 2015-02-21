# 2nd attempt at Proj. Euler #25

import pyperclip

def nextFib(n1, n2): # n1 is the Nth-1 term and n2 is the Nth-2 term
    n = n1 + n2 
    return(n) # n is the Nth term

def checkLength(n): # Checks number of digits in an integer
    n = str(n)
    length = len(n)
    return length

terms = [1, 1]

while checkLength(terms[len(terms) - 1]) != 1000:
    terms.append(nextFib(terms[len(terms) - 1], terms[len(terms) - 2]))

print(len(terms))

