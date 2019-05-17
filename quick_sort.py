#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
quick sort algo
"""

def qs(arr):
    """ entry point to perform quick sore
    """
    print("before quick sort {}".format(arr))
    rqs(arr, 0, len(arr)-1)
    print("after quick sort {}".format(arr))

def rqs(arr, begin, end):
    """ recursive qs function
    """
    pivotIdx = 0
    if begin < end:
        pivotIdx = partition(arr, begin, end)
        rqs(arr, 0, pivotIdx - 1)
        rqs(arr, pivotIdx + 1, end)

def partition(arr, begin, end):
    """ function to find the correct position for the pivot Value
    """
    pIdx = begin
    pVal = arr[end]

    while begin < end:
        if arr[begin] < pVal:
            arr[begin], arr[pIdx] = arr[pIdx], arr[begin]
            pIdx += 1
        begin += 1
    arr[begin], arr[pIdx] = arr[pIdx], arr[begin]
    return pIdx

if __name__ == '__main__':
    qs([15,76,2,4,7,23,55,79])
    print("-----------")
    qs([1,2,3])
    print("-----------")
    qs([7,5,3])
    print("-----------")
    qs([3,1])
    print("-----------")
    qs([1])
    