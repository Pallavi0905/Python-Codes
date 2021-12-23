# method1
def reverse(lst):
    lst.reverse()
    return lst

lst = [12,34,56,78,90]
print(reverse(lst))

# method2
def reverse(lst):
    newLst = lst[::-1]
    return newLst
