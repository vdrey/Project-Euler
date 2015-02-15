# Third attept project euler #5


# THIS WORKS

def divCheck(n):

    for i in range(1,21):
        if n%i != 0:
            return False 

    return True

n = 2

while not divCheck(n):
    n += 2

print(n)
