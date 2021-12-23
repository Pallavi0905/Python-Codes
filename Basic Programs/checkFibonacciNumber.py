import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

for i in range(1, 20):
    if (isFibonacci(i)==True):
        print (f"{i} is a Fibonacci Number")
        # i, "is a Fibonacci Number"
    else:
        print (f"{i} is not a Fibonacci Number")
        # print i, "is not a Fibonacci Number"