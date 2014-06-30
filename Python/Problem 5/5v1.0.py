# First attempt at problem 5

import math
testNum = 12252240

def factorCheck(num):

    factorList = [18,19,20] #[11,12,13,14,15,16,17,18,19,20]
    score = 0

    for term in factorList:

        if num % term == 0:
            score = score + 1

        else:
            break

    if score == 3:
        return True

    else:
        return False


#Now use the definition

while testNum < 20000000000000000000:

    print(testNum)

    if factorCheck(testNum) == True:
        answer = testNum
        break

    else:
        testNum = testNum + 12252240
        

print(answer)
