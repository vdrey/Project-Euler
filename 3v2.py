# Problem 3

n = 0
TARGET = 600851475143
rnd1 = []
currTerm = 599851475143 

while n < 100000:

    if currTerm/2 == int(currTerm/2):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/3 == int(currTerm/3):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/5 == int(currTerm/5):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/7 == int(currTerm/7):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/11 == int(currTerm/11):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/13 == int(currTerm/13):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/17 == int(currTerm/17):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/19 == int(currTerm/19):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/23 == int(currTerm/23):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/29 == int(currTerm/29):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/31 == int(currTerm/31):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/37 == int(currTerm/37):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/41 == int(currTerm/41):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/43 == int(currTerm/43):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/47 == int(currTerm/47):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/53 == int(currTerm/53):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/59 == int(currTerm/59):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/61 == int(currTerm/61):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/67 == int(currTerm/67):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/71 == int(currTerm/71):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/79 == int(currTerm/79):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/83 == int(currTerm/83):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/89 == int(currTerm/89):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/97 == int(currTerm/97):
        n = n + 1
        currTerm = currTerm - 1

    elif currTerm/101 == int(currTerm/101):
        n = n + 1
        currTerm = currTerm - 1

    else:
        rnd1.append(currTerm)
        print(currTerm)
        n = n + 1
        currTerm = currTerm -1

print(len(rnd1))
