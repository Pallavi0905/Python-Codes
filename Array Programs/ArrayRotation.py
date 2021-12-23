# method 1 - temp array
# Function to rotate array by d element using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while(i<d):
        temp.append(arr[i])
        i = i+1
    i = 0
    while(d<n):
        arr[i]= arr[d]
        i = i+1
        d = d+1
    arr[:]=arr[: i]+ temp
    return arr

arr = [1,2,3,4,5,65,43,55,76]
print("Array after left position is ", end=' ')
print(rotateArray(arr, len(arr), 2))

# method 2 - rotate one by one
def leftRotate(arr,d,n):
    for i in range(d):
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i]= arr[i+1]
    arr[n-1]=temp

def printArray(arr,size):
    for i in range(size):
        print("%d"% arr[i], end=" ")

arr = [1,2,3,4,5,65,43,55,76]
leftRotate(arr,2,9)
printArray(arr,9)

# method 3 - using list slicing
def rotateList(arr, d, n):
    arr[:]= arr[d:n]+arr[0:d]
    return arr

arr = [1,2,3,4,5,65,43,55,76]
print("Rotate List is ")
print(rotateList(arr,2,len(arr)))