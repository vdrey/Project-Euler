# First try at problem 6

numSet = []
n = 1

while n <= 1000:

    numSet.append(n)
    n = n + 1

setSum = sum(numSet)
setSumSq = setSum ** 2

print(setSumSq - setSum)

#Misread begin work on v2
