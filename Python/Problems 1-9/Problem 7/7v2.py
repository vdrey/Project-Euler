# 7v2
def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False

    return [2]+[i for i in range(3,n,2) if sieve[i]]

pList = [2,3]
currTerm = 4

while len(pList) < 10:

    if primes(currTerm) == True:
        pList.append(currTerm)
        currTerm = currTerm + 1

    else:
        currTerm = currTerm + 1
