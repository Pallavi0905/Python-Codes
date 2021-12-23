testList = [12,23,43,54,65,76]

print("Checking if 4 exists in the list (using loop) : ")
for i in testList:
    if(i == 43):
        print("Element Exists")

print("Checking if 4 exists in list (using in ) : ")
if (23 in testList):
    print("Element exists")