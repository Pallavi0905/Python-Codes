# Fibonacci series, Fn = Fn-1 + Fn-2
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
def fibonacci(n):
    if n<0:
        print("Incorrect Input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))