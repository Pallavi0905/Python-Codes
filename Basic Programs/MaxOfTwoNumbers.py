# method1
num1 = input("Enter the num1: ")
num2 = input("Enter the num2: ")

maximum = max(num1,num2)
print(f"The maximum number between {num1} and {num2} is {maximum}")

# method2
def maximum(num1, num2):
    if num1>=num2:
        return num1
    else:
        return num2
num1 = input("Enter the num1: ")
num2 = input("Enter the num2: ")
print(f"The maximum of {num1} and {num2} is {maximum(num1, num2)}.")