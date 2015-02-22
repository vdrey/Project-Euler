# The second try at problem 6

n = 1
numList = []
sqList = []

while n <= 100:
    numList.append(n)
    n = n + 1

n = 1

while n <= 100:
    sqList.append(n ** 2)
    n = n + 1

sumNum = sum(numList)
sumNumSq = sumNum ** 2

sumSq = sum(sqList)

print(sumNumSq - sumSq)
