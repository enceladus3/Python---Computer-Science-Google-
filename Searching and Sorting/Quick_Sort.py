"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    quicksort2(array, 0, len(array)-1)
    return array
    
def quicksort2(array, low, hi):
    if low < hi:
        p = partition(array, low, hi)
        quicksort2(array, low, p-1)
        quicksort2(array, p+1, hi)

def getPivot(array, low, hi):
    mid = (hi+low) // 2
    s = sorted([array[low], array[mid], array[hi]])
    if s[1] == array[low]:
        return low
    elif s[1] == array[mid]:
        return mid
    return hi
    
def partition (array, low, hi):
    pivotIndex = getPivot(array, low, hi)
    pivotValue = array[pivotIndex]
    array[pivotIndex], array[low] = array[low], array[pivotIndex]
    border = low
    
    for i in range(low, hi+1):
        if array[i] < pivotValue:
            border += 1
            array[i], array[border] = array[border], array[i]
    array[low], array[border] = array[border], array[low]
    return (border)
        


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print quicksort(test)
