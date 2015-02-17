#Problem 4 solution v1

def reverse(num):
  return int(str(num)[::-1])

a = 100
y = []

while a < 1000:

    b = 100

    while b < 1000:

        if a * b == reverse(a * b):
            y.append(a*b)
            b = b + 1

        else:
            b = b +1

    a = a + 1


y.sort()

x = y[len(y) - 1]

print(x)
