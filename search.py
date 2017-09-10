def linearSearch(array, value):
    found = False
    index = 0
    while found == False and index < len(array):
        if array[index] == value:
            found = True
        else:
            index = index + 1
    if found == True:
        return index
    else:
        return -1  # not found
        
def binarySearchIterative(array, value):
    found = False
    begin = 0
    end = len(array)
    while found == False and begin < end:
        mid = (begin + end) // 2
        if array[mid] == value:
            found = True
        elif array[mid] < value:
            begin = mid + 1
        else:
            end = mid
    if found == True:
        return mid
    else:
        return -1  # not found
        
def binarySearchRecursive(array, value, begin = None, end = None):
    if begin == None:
        begin = 0
    if end == None:
        end = len(array)
    if begin < end:
        mid = (begin + end) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            return binarySearchRecursive(array, value, mid + 1, end)
        else:
            return binarySearchRecursive(array, value, begin, mid)
    else:
        return -1  # not found
