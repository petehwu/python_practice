#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
binary search algo
"""
"""input = [
    'mission statement',
    'a quick bite to eat',
    'a chip off the old block',
    'chocolate bar',
    'mission impossible',
    'a man on a mission',
    'block party',
    'eat my words',
    'bar of soap'
]
output = [
    'a quick bite to eat my words',
    'a chip off the old block party',
    'chocolate bar of soap',
    'a man on a mission statement',

"""


def concat(arr):
    d = {}
    ans = []
    for idx, s in enumerate(arr):
        k = s.split()[0]
        if k not in d:
            d[k] = [idx]
        else:
            d[k].append(idx)
    for s in arr:
        v = s.split()[-1]
        s = " ".join(s.split()[:-1])
        if v in d:
            for x in d[v]:
                ans.append("{} {}".format(s, arr[x]))
    print(*ans, sep=",\n")


if __name__ == '__main__':
    input = [
        'mission statement',
        'a quick bite to eat',
        'a chip off the old block',
        'chocolate bar',
        'mission impossible',
        'a man on a mission',
        'block party',
        'eat my words',
        'bar of soap'
    ]
    concat(input)
