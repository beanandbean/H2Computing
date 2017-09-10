def bubbleSortInefficient(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp

def bubbleSortStandard(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
                
def bubbleSortEfficient(array):
    i = 0
    swapped = True
    while swapped == True and i < len(array):
        swapped = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
                swapped = True

def insertionSort(array):
    for i in range(1, len(array)):
        j = 0
        while j < i and array[j] <= array[i]:
            j = j + 1
        if j < i:
            tmp = array[i]
            for k in range(i, j, -1):
                array[k] = array[k - 1]
            array[j] = tmp
            
def quickSort(array, begin = None, end = None):
    if begin == None:
        begin = 0
    if end == None:
        end = len(array)
    if begin < end - 1:
        pivot = begin
        left = begin
        right = end
        while left < right - 1:
            if array[left + 1] <= array[pivot]:
                left = left + 1
            elif array[right - 1] > array[pivot]:
                right = right - 1
            else:
                tmp = array[left + 1]
                array[left + 1] = array[right - 1]
                array[right - 1] = tmp
        if left > pivot:
            tmp = array[left]
            array[left] = array[pivot]
            array[pivot] = tmp
        quickSort(array, begin, left)
        quickSort(array, left + 1, end)
    
