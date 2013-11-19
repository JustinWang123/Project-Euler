def IsDivisiblePrimes(n, primes):
    for i in primes:
        if n % i != 0:
            return False
    return True

def IsDivisible(n):
    for i in range(2, 20):
        if n % i != 0:
            return False
    return True

primes = [2, 3, 5, 7, 11, 13, 17, 19]
primeProduct = 1

for i in primes:
    primeProduct *= i

for i in range(1, 1000):
    if IsDivisible(i * primeProduct):
            print(i * primeProduct)
            break
