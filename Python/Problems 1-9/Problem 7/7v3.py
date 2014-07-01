#7v3

import re, sys


def isPrime(n):
    # see http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None


N = int(sys.argv[1]) # number of primes wanted (from command-line)
M = 100              # upper-bound of search space
list = []           # result list

while len(l) < 10001:
    l += filter(isPrime, range(M - 100, M)) # append prime element of [M - 100, M] to l
    M += 100                                # increment upper-bound

print l[:10001] # print result list limited to N elements
