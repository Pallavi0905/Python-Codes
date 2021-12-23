from functools import reduce
l = [1,5,8,3]

a = reduce(max, l)
print(a)