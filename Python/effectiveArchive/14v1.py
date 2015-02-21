# First attempt at Proj. Euler number 14

def even(n): # if n is even, this returns n/2
    term = n / 2
    return term

def odd(n): # if n is odd, this returns 3n + 1
    term = 3 * n
    term += 1
    return term

maxChain = 0
startMax = 0

for i in range(1,1000001):
    num = i
    chain = 0
    if num % 1000 == 0:
        print(num)
    while num != 1:
        if num % 2 == 0:
            num = even(num)
            chain += 1
        else:
            num = odd(num)
            chain += 1
    if chain > maxChain:
        maxChain = chain
        startMax = i

print(startMax)
