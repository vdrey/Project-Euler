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
