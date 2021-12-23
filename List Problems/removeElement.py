list = [11,23,43,54,24]
list = [elem for elem in list if elem % 2 != 0]
print(*list)

del list[1:3]
print(*list)

list = [11,23,43,54,24]
unwanted = [23,43]
for ele in sorted(unwanted, reverse= True):
    del list[ele]
print (*list)