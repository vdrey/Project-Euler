# First attempt of problem 25

#[1, 2, 3, 5,...]
#[a, x, y, z,...]

z = 5
y = 3
x = 2
terms = [1,2,3,]
insif = False

while len(str(terms[len(terms)-1])) < 1000:

    if insif == True: #to find nth term, use a len statement
        break

    else:
        terms.append(z)
        a = x
        b = y
        c = z
        z = b + c
        y = b + a
        x = b
        print(len(str(terms[len(terms)-1])))

print(terms[len(terms)-1])
