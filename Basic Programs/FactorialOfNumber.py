# factorial, n!= n X (n-1) X (n-2) ....
#            n! = n X (n-1)!
def factorial(n):
    #method1
    return 1 if n==0 or n==1 else n*factorial(n-1)

    #method2
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

a = int(input("Enter the number you want to fine the factorial of: "))
print(f"The factorial of {a} if {factorial(a)}")
