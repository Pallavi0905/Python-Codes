def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    
    result = []
    i,j = 0, 0
    while (len(result)<len(left)+len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j+=1
        if i==len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

def mergeSort(list):
    if len(list) <2:
        return list
    middle = len(list)/2
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])

    return merge(left, right)

seq = [12,11,23,43,54,23,43,13]
print("Given array is:")
print(seq)
print("\n")
print("Sorted array is")
print(mergeSort(seq))