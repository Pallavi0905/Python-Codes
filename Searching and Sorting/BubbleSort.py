def BubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]

arr = [12,54,34,87,56,0,35]
BubbleSort(arr)
print("Sorted array:")
for i in range(len(arr)):
    print("%d" %arr[i])