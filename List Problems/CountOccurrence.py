def countX(lst,x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count +1
    return count

lst = [11,23,23,45,23,45,65]
x=23
print(f"{x} has occured {countX(lst,x)} times")

# method2
def countX(lst, x):
    return lst.count(x)

# method3
from collections import Counter
l = [1,1,2,2,2,2,2,2,3,3,3]
x=2
d = Counter(l)
print(d)