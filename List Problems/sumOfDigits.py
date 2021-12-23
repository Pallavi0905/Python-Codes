from functools import reduce
list1 = [12,34,54,65,76]
print("The original list is : " + str(list1))

res = [reduce(lambda x,y : int(x)+int(y), list(str(i))) for i in list1]
print("The sum of the digits of the given list is: " + str(res))