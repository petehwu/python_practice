#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
binary search algo
"""


from math import floor
def binsearch(arr, v):
    """ entry point for binary search
    """
    idx = bs(arr, 0, len(arr)-1, v)
    if idx is None:
        print("Number {} not in list {}".format(v, arr))
    else:
        print("Number {} found at index {} in list {}".format(v, idx, arr))


def bs(arr, left, right, v):
    """ recursive binary search
    """
    if left > right:
        return None
    m = (left + right)//2
    if v == arr[m]:
        return m
    elif v > arr[m]:
        return(bs(arr, m + 1, right, v))
    else:
        return(bs(arr, 0, m - 1, v))

k
if __name__ == '__main__':
    binsearch([0,1,2,3,4,5,9, 10, 15, 20], 0)
    binsearch([0,1,2,3,4,5,9, 10, 15, 20], 1)
    binsearch([0,1,2,3,4,5,9, 10, 15, 20], 3)
    binsearch([0,1,2,3,4,5,9, 10, 15, 20], 20)
    binsearch([0,1,2,3,4,5,9, 10, 15, 20], 50)
    binsearch([0], 50)
    binsearch([0], 0)
    binsearch([0,1], 0)
    binsearch([0,1], 3)

