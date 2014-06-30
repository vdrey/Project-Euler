# The second try at problem 6

n = 1
numList = []
sqList = []

while n <= 1000:
    numList.append(n)
    n = n + 1

n = 1

while n <= 1000:
    sqList.append(n ** 2)
    n = n + 1

sumNum = sum(numList)

