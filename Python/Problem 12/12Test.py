def genTri(terms): # This works
    vals = []
    n = 0
    while len(vals) <= terms:
        nextTerm = 0
        for i in range(n+1):
            nextTerm += i
        vals.append(nextTerm)
        n += 1
    return vals

# print(genTri(70)) 

def getNumDivisors(num): # This works
    divs = []
    for i in range(1, num // 2):
        if num % i == 0:
            if i not in divs:
                divs.append(i)
            if num // i not in divs:
                divs.append(num // i)
    return len(divs)

# print(getNumDivisors(2800))

def nextTri(currentTerm, currentInt): # This works
    n = currentInt + 1
    nextTerm = currentTerm + n
    return nextTerm

r = 0
term = 0
while r < 100:
    print(nextTri(term, r))
    term = nextTri(term, r)
    r += 1

