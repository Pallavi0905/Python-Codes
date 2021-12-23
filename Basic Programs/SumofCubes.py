# method 1
def cubeSum(n):
    return (n*(n+1))**2//4

x=3
print(cubeSum(x))

# method 2
def cubeSum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i*i*i)
    return sum

x=3
print(cubeSum(x))