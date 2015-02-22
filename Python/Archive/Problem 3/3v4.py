# Problem 3 with the Sieve of Eratosthenes to find primes



# List of definitions
'''
TARGET = list primes less than this number
primes = list of generated primes--only used untill squrt(TARGET) reached
currTerm = the number that is being checked for primality
terms = list of all numbers < TARGET--becomes list of all
        primes once sieve is complete
pFactors = factors of TARGET from terms post-sieve
           To be generated in reverse order (largest factor first)
'''

# To find target number
print('What is your target number?')
TARGET = input()
TARGET = int(TARGET)

# To generate list of numbers less than TARGET (excluding evens)
ax = 3
terms = []

while ax < int(TARGET * .001):

    terms.append(ax)
    ax = ax + 2

print('List of odd numbers less than .1% of ' + str(TARGET) + ' generated')


# Sieve of Eratosthenes (modified) time
'''
n = nth term in list(terms)
a = nth term in list(primes)
b = binary status indicator if n has been proven to be un-prime
    1 means it has
    2 means it hasn't
'''
primes = [3, 5]
n = 0

while n < len(terms):

    a = 0
    b = 2
    
    while a < (len(primes)-1):

        if terms[n]/primes[a] == int(terms[n]/primes[a]):
            n = n + 1
            a = (len(primes)-1)
            b = 1
            break

        else:
            a = a + 1

    while a == (len(primes)-1):

        if b == 1:
            break
        
        elif terms[n]/primes[a] == int(terms[n]/primes[a]):
            n = n + 1
            break

        else:
            primes.append(terms[n])
            n = n + 1

print('List of the ' + str(len(primes)) + ' primes less than ' + str(TARGET) + ' found')

# Reverse primes list
primes.reverse()
print('The prime list has been reversed')

# Find prime factors of TARGET (only print the largest one)
'''
c = nth term in primes (remember, largest first)
'''
pFactors = []
c = int(.001*TARGET)

while c < len(primes):

    if TARGET/primes[c] == int(TARGET/primes[c]):
        pFactors.append(primes[c])
        break

    else:
        c = c + 1

print(pFactors)
