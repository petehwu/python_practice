#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
binary search tree implementation
"""


def bubbleSort(arr):
    """ bubble sort algo
    """
    swapped = True
    print("before bubble sort {}".format(arr))
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    print("after bubble sort {}".format(arr))


def quickSort(arr):
    """ quick sort entry point
    """
    print("before quickSort {}".format(arr))
    rqs(arr, 0, len(arr) - 1)
    print("after quickSort {}".format(arr))


def rqs(arr, begin, end):
    """ recursive quick sort algo
    """
    if begin < end:
        pIndex = findPivot(arr, 0, end)
        rqs(arr, 0, pIndex - 1)
        rqs(arr, pIndex + 1, end)


def findPivot(arr, begin, end):
    pIndex = begin
    pVal = arr[end]
    while begin < end:
        if arr[begin] < pVal:
            arr[begin], arr[pIndex] = arr[pIndex], arr[begin]
            pIndex += 1
        begin += 1
    arr[begin], arr[pIndex] = arr[pIndex], arr[begin]
    return pIndex


def mergeSort(arr):
    """ entry point for merge sort
    """
    print("before merge sort {}".format(arr))
    rms(arr)
    print("after merge sort {}".format(arr))


def rms(arr):
    """recursive merge sort algo
    """
    mid = len(arr) // 2
    if mid > 0:
        left = arr[:mid]
        right = arr[mid:]
        rms(left)
        rms(right)
        merge(arr, left, right)


def merge(arr, left, right):
    """ merge left and right for merge sort
    """
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
        li += 1
        ai += 1
    while ri < len(right):
        arr[ai] = right[ri]
        ri += 1
        ai += 1


if __name__ == '__main__':
    bubbleSort([50, 90, 23, 56, 1, 3, 7, 45, 7, 8])
    quickSort([50, 90, 23, 56, 1, 3, 7, 45, 7, 8])
    mergeSort([50, 90, 23, 56, 1, 3, 7, 45, 7, 8])
    print("++++++++++++++++")
    bubbleSort([1, 2, 3])
    quickSort([1, 2, 3])
    mergeSort([1, 2, 3])
    print("++++++++++++++++")
    bubbleSort([1])
    quickSort([1])
    mergeSort([1])
    print("++++++++++++++++")
    bubbleSort([1, 2])
    quickSort([1, 2])
    mergeSort([1, 2])
    print("++++++++++++++++")
    bubbleSort([3, 2, 1])
    quickSort([3, 2, 1])
    mergeSort([3, 2, 1])
    print("++++++++++++++++")
