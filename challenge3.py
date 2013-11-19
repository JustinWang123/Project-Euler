# find the largest prime factor of 600851475143

import math

def IsPrime(n):
    for i in range(2, math.ceil(n**(1/2))):
        if n % i == 0:
            return False
    return True

number = 600851475143
largestFactor = 1

while number > 1:
    for i in range(2, number + 1):
        if number % i == 0 and IsPrime(i):
            largestFactor = i
            number = math.floor(number / largestFactor)
            break

print(largestFactor)
