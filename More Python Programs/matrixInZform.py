arr = [[1,3,5,7],[3,4,5,7],[7,6,5,1],[8,9,5,0]]
n = len(arr[0])
i = 0
for j in range(0,n-1):
    print(arr[i][j],end=" ")
k=1
for i in range(0,n):
    for j in range(n,0,-1):
        if (j==n-k):
            print(arr[i][j],end=" ")
            break
    k+=1
i=n-1
for j in range(0,n):
    print(arr[i][j],end=" ")