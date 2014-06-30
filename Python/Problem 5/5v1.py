# First attempt at problem 5

import math
testNum = math.factorial(20) - (2520 * 11)

def factorCheck(num):

    factorList = [11,12,13,14,15,16,17,18,19,20]
    score = 0

    for term in factorList:

        if num % term == 0:
            score = score + 1

        else:
            break

    if score == 10:
        return True

    else:
        return False


#Now use the definition

while testNum > 2000000:

    print(testNum)

    if factorCheck(testNum) == True:
        answer = testNum
        break

    else:
        testNum = testNum - (2520 * 11)
        

print(answer)
