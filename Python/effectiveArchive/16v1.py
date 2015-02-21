# First attempt at Proj. Euler number 16

NUM = str(2**1000)
digs = []
start = 0
end = 1

while end <= len(NUM):
    digs.append(int(NUM[start:end]))
    start += 1
    end += 1

sumDigs = sum(digs)
print(sumDigs)
