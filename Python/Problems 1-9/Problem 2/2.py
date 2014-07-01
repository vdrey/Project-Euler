# this is to solve project Euler problem 2


print('Press enter.')
#input()

z = 5
y = 3
x = 2
terms = [1,2,3,]
evenTerms = [2]

while z <= 4000000:

    if z/2 == int(z/2):
        evenTerms.append(z)
        terms.append(z)
        a = x
        b = y
        c = z
        z = b + c
        y = b + a
        x = b
        print(evenTerms)
        
    elif z + y > 4000000: 
        break

    

    else:
        terms.append(z)
        a = x
        b = y
        c = z
        z = b + c
        y = b + a
        x = b


print('And the sum of the terms is....')

print(sum(evenTerms))
