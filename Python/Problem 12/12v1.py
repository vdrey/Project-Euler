# This is the first attempt at Proj. Euler number 12

def getNumDivisors(num): # This works
    divs = []
    for i in range(1, num // 2):
        if num % i == 0:
            if i not in divs:
                divs.append(i)
            if num // i not in divs:
                divs.append(num // i)
    return len(divs)

def nextTri(currentTerm, currentInt): # This works
    n = currentInt + 1
    nextTerm = currentTerm + n
    return nextTerm

term = 17907120 # 480 divisors
counter = 5984
while getNumDivisors(term) <= 500:
    term = nextTri(term, counter)
    counter += 1
    

print('counter: %s' % (counter))
print()
print()
print('divisors: %s' % (getNumDivisors(term)))
print()
print()
print(term)
