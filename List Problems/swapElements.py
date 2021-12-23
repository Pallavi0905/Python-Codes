# method1
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

List = [23,34,56,45,76,77]
pos1, pos2 = 1,3
print(swapPositions(List, pos1-1, pos2-1))

# method2
def swapPositions(list, pos1, pos2):
    get = list[pos1], list[pos2]
    list[pos2], list[pos1] = get
    return list

List = [23,34,56,45,76,77]
pos1, pos2 = 1,3
print(swapPositions(List, pos1-1, pos2-1))

# method3
def swapPositions(list, pos1, pos2):
    first=list.pop(pos1)
    second=list.pop(pos2-1)

    list.insert(pos1, second)
    list.insert(pos2, first)
    return list

List = [23,34,56,45,76,77]
pos1, pos2 = 1,3
print(swapPositions(List, pos1-1, pos2-1))
