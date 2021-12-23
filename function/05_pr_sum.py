#def sum_iter(n):
#    product = 0
#    for i in range(n):
#        sum = sum + (i+1)
#    return sum

def sum_recursive(n):
    if n<=1:
        return n
    return n + sum_recursive(n-1)

s = sum_recursive(10)
print(s)