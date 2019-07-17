#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
quick sort
"""


def qs(arr):
    """ entry point to quick sort
    """
    print("before {}".format(arr))
    qqs(arr, 0, len(arr) - 1)
    print("after {}".format(arr))


def qqs(arr, start, end):
    """ recursive query for quick sort
    """
    pivotIndex = 0
    if start < end:
        pivotIndex = partition(arr, start, end)
        qqs(arr, 0, pivotIndex - 1)
        qqs(arr, pivotIndex + 1, end)


def partition(arr, start, end):
    """ find the correct spot for the pivot value
    """
    pIndex = start
    pVal = arr[end]
    while start < end:
        if arr[start] < pVal:
            arr[start], arr[pIndex] = arr[pIndex], arr[start]
            pIndex += 1
        start +=  1
    arr[start], arr[pIndex] = arr[pIndex], arr[start]
    return pIndex


def ms(arr):
    """ entry point for merge sort
    """
    print("before {}".format(arr))
    mms(arr)
    print("after {}".format(arr))

def mms(arr):
    """recursive query for merge sort
    """
    mid = len(arr) // 2
    if mid > 0:
        left = arr[:mid]
        right = arr[mid:]
        mms(left)
        mms(right)
        merge(arr, left, right)

def merge(arr, left, right):
    lidx = 0
    ridx = 0
    aidx = 0

    while lidx < len(left) and ridx < len(right):
        if left[lidx] < right[ridx]:
            arr[aidx] = left[lidx]
            lidx += 1
        else:
            arr[aidx] = right[ridx]
            ridx += 1
        aidx += 1
    while lidx < len(left):
        arr[aidx] = left[lidx]
        lidx += 1
        aidx += 1
    while ridx < len(right):
        arr[aidx] = right[ridx]
        ridx += 1
        aidx += 1

if __name__ == '__main__':
    print("----------")
    qs([5,3,8,9,5,3,1,10,100])
    ms([5,3,8,9,5,3,1,10,100])
    print("----------")
    qs([5,3])
    ms([5,3])
    print("----------")
    qs([5])
    ms([5])
        


