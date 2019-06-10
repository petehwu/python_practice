#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
quick way to sort a dictionary
"""


def sortByKey(d):
    """ Sort dictionary by key
    """
    b = dict(sorted(d.items(), key=lambda x: x[0]))
    print("{} sorted by key is\n {}".format(d, b))


def sortByVal(d):
    """ Sort dictionary by value
    """
    b = dict(sorted(d.items(), key=lambda x: x[1]))
    print("{} sorted by value is\n {}".format(d, b))


def sortByKeyVal(d):
    """ Sort dictionary by key then value
    """
    b = dict(sorted(d.items(), key=lambda x: (x[0], x[1]))) 
    print("{} sorted by key then value is\n {}".format(d, b))


def sortByValKey(d):
    """ Sort dictionary by value then key
    """
    b = dict(sorted(d.items(), key=lambda x: (x[1], x[0])))
    print("{} sorted by value then key is\n {}".format(d, b))


if __name__ == '__main__':
    di = {"c": 5, "b": 3, "d": 8, "a": 2, "e": 5}
    sortByKey(di)
    sortByVal(di)
    sortByKeyVal(di)
    sortByValKey(di)
