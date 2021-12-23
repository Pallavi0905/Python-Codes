# method 1
def productuniquefactors(n):
    product = 1
    for i in range(2, n+1):
        if (n%i==0):
            isPrime = 1
            for j in range(2, int(i/2+1)):
                if (i%j==0):
                    isPrime = 0
                    break
            if (isPrime):
                product = product * i
    return product

n=63
print(productuniquefactors(n))

'''-------------------------------------'''

#method2
import math
def productuniquefactors(n):
    product = 1
    if (n%2==0):
        while(n%2==0):
            n=n/2
    for i in range(3, int(math.sqrt(n)),2):
        if (n%i==0):
            product = product * i
            while(n%i==0):
                n=n/i
    if(n>2):
        product = product * n
    return product

n=28
print(int(productuniquefactors(n)))