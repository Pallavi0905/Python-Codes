# method1
list1 = [12,34,23,9,5,6,78,7]
list1.sort()
print("Smallest element is: ", *list1[:1])

# method2
list1 = [12,34,23,9,5,6,78,7]
print("The smallest element in the list is: ", min(list1))