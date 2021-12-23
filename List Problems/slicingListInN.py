myList = [1,2,3,4,5,6,7,8]
n=2
final = [myList[i*n:(i+1)*n] for i in range((len(myList) + n-1)//n)]
print(final)

# method2
# x = [l[i:i+n] for i in range(0, len(l),n)]