total = 0
list1=[23,43,54,12,21]

for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)

# method2
list1 = [11,23,24,32,41]

def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size-1] + sumOfList(list, size-1)
total = sumOfList(list1, len(list1))
print("Sum of the element of the list: ", total)