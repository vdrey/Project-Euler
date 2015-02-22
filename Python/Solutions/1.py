# find the sum of all natural-number multiples of 3 or 5 below 1000


#sum of multiples of 3

mthree = 1
lthree = []

while mthree < 334:

    lthree.append(3*mthree)
    mthree = mthree + 1

sumthree = sum(lthree)

#sum of multiples of 5

mfive = 1
lfive =[]

while mfive < 200:

    lfive.append(5*mfive)
    mfive = mfive + 1

sumfive = sum(lfive)


#sum of multiples of 15

mfifteen = 1
lfifteen = []

while mfifteen < 67:
    lfifteen.append(15*mfifteen)
    mfifteen = mfifteen + 1

    
sumfifteen = sum(lfifteen)


# Final total

print(sumthree + sumfive - sumfifteen)






#it worked
