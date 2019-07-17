#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
sort practice
"""

def qs(arr):
    """entry point for quick sort
    """
    print("before sorting {}".format(arr))
    rqs(arr, 0, len(arr) - 1)
    print("after sorting {}".format(arr))

def rqs(arr, start, end):
    pIndex = 0
    if start < end:
        pIndex = findPivot(arr, start, end)
        rqs(arr, 0, pIndex-1)
        rqs(arr, pIndex+1, end)

def findPivot(arr, start, end):
    pIndex = start
    pVal = arr[end]
    while start < end:
        if arr[start] < pVal:
            arr[start], arr[pIndex] = arr[pIndex], arr[start]
            pIndex += 1
        start += 1
    arr[start], arr[pIndex] = arr[pIndex], arr[start]
    return pIndex


def ms(arr):
    """ entry point for merge sort
    """
    print("before sort {}".format(arr))
    rms(arr)
    print("after sort {}".format(arr))

def rms(arr):
    mid = len(arr) // 2
    if mid > 0:
        left = arr[0:mid]
        right = arr[mid:]
        rms(left)
        rms(right)
        merge(arr, left, right)
    
def merge(arr, left, right):
    ai = 0
    li = 0
    ri = 0
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            arr[ai] = left[li]
            li += 1
        else:
            arr[ai] = right[ri]
            ri += 1
        ai += 1
    while li < len(left):
        arr[ai] = left[li]
        ai += 1
        li += 1
    while ri < len(right):
        arr[ai] = right[ri]
        ai += 1
        ri += 1


if __name__ == '__main__':
    qs([4,3,6,5,2,7,8,1, 10, 45,67])
    qs([1])
    qs([2,1])
    ms([4,3,6,5,2,7,8,1, 10, 45,67])
    ms([1])
    ms([2,1])

