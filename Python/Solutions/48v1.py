# First attempt at number 48

nums = []
for i in range(1, 1001):
    nums.append(i**i)

series = str(sum(nums))
print(series)
print(series[len(series)-10:len(series)])
