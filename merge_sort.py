#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
merge sort algo
"""

def ms(arr):
    """ entry point for merge sort
    """
    print ("before merge sort {}".format(arr))
    rms(arr)
    print ("after merge sort {}".format(arr))

def rms(arr):
    """ recursive function that keep splitting the list till 1 element in left and right
    """
    mid = len(arr) // 2
    if mid > 0:
        left = arr[0:mid]
        right = arr[mid:]
        rms(left)
        rms(right)
        mergeLR(arr, left, right)

def mergeLR(arr, left, right):
    """merges the left and right into one orderd list
    """
    lIdx = 0
    rIdx = 0
    aIdx = 0
    while lIdx < len(left) and rIdx < len(right):
        if left[lIdx] < right[rIdx]:
            arr[aIdx] = left[lIdx]
            lIdx += 1
        else:
            arr[aIdx] = right[rIdx]
            rIdx += 1
        aIdx += 1
    while lIdx < len(left):
        arr[aIdx] = left[lIdx]
        lIdx += 1
        aIdx += 1
    while rIdx < len(right):
        arr[aIdx] = right[rIdx]
        rIdx += 1
        aIdx += 1

if __name__ == '__main__':
    ms([20,45,78,23,6,7,2,8,13,77])
    print("-----")
    ms([1, 2, 3])
    print("-----")
    ms([1])
    print("-----")
    ms([1,2])
    print("-----")
    ms([2, 1])
    print("-----")
