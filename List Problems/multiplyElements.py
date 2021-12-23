def multiplyElements(myList):
    result = 1
    for x in myList:
        result = result*x
    return result

list1= [11,2,3,2]
list2 = [3,3,4,5]
print(multiplyElements(list1))
print(multiplyElements(list2))

# method2
# import numpy
list1= [11,2,3,2]
list2 = [3,3,4,5]

# result1 = numpy.prod(list1)
# result2 = numpy.prod(list2)
# print(result1)
# print(result2)

# method3
from functools import reduce
list1= [11,2,3,2]
list2 = [3,3,4,5]

result1 = reduce((lambda x,y:x*y), list1)
result2 = reduce((lambda x,y:x*y), list2)
print(result1)
print(result2)