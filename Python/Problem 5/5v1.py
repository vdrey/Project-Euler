# First attempt at problem 5

import math
testNum = 2520
index = 0
answers = [2520]

def factorCheck(num):

    indexCheck = 0
    factorList = [11,12,13,14,15,16,17,18,19,20]
    score = 0

    for term in factorList:

        if num % term == 0:
            score = score + 1

        else:
            break

    if score == (indexCheck + 1):
        indexCheck = indexCheck + 1
        return True

    else:
        return False


#Now use the definition

while testNum < 20000000000000000000 and index <= 10:

    print(str(answers) + ' ' + str(testNum))

    if factorCheck(testNum) == True:
        index = index + 1
        answers.append(testNum)

    else:
        testNum = testNum + answers[len(answers) -1]
        

print(answers)
