def largest(arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
    return max

arr = [23,234,543,568,37,569]
n= len(arr)
ans = largest(arr,n)
print("The largest element of array is ", ans)