# First attempt at problem 5

testNum = 2000000

def factorCheck(num):

    factorList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    score = 0

    for term in factorList:

        if num % term == 0:
            score = score + 1

        else:
            break

    if score == 20:
        return True

    else:
        return False


#Now use the definition

while testNum < 1234567890:

    print(testNum)

    if factorCheck(testNum) == True:
        answer = testNum
        break

    else:
        testNum = testNum + 20
        

print(answer)
