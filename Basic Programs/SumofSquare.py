# method1
def squaresum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i*i)
    return sum

x=2
print(squaresum(x))

# method 2
def squaresum(n):
    return (n*(n+1)*(2*n+1))//6

x=2
print(squaresum(x))