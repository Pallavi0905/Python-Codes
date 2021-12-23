def splitArr(a, n, k):
    b = a[:k]
    return(a[k::]+b[::])

arr = [12,34,25,35,65,78]
n = len(arr)
position = 3
arr = splitArr(arr, n, position)
for i in range(0, n):
    print(arr[i], end=' ')