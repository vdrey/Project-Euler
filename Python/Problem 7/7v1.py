# This is the first attempt at problem 7

insif = 0

trial = 30 # Trial--ie number being tried

primes = [2,3,5,7,11,13,17,19,23,29]

while len(primes) < 10000:

    print(len(primes))
    currLength = len(primes)

    for term in primes:

        if trial % term == 0:
            trial = trial + 1
            break

        elif primes.index(term) == (len(primes) - 1) and trial % term != 0:
            primes.append(trial)
            trial = trial + 1
            

        else:
            insif = insif + 1

print('This is the 10001th prime ' + str(primes[10001]))
print()
print('This number is insif ' + str(insif))
    
