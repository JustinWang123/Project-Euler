def SumOfSquares(n):
    theSum = 0
    for i in range(1, n+1):
        theSum += i**2
    return theSum

def SquareOfSum(n):
    theSum = 0
    for i in range(1, n+1):
        theSum += i
    return theSum**2

print(SquareOfSum(100))
print(SumOfSquares(100))
print(SquareOfSum(100) - SumOfSquares(100))
