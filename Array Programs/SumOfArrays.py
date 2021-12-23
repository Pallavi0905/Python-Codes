# method 1
def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum+i
    return sum

arr = []
arr = [2,4,35,65]
n = len(arr)
ans = _sum(arr)
print("Sum of the array is ", ans)

# method 2
arr = []
arr = [2,45,34,23]

ans = sum(arr)
print("The sum of the element of an array is ", ans)