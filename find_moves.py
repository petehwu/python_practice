#!/Users/pwu/anaconda/bin/python3
""" shebang for linux #!/usr/bin/env python3
find number of moves to punch in a numeric string
"""


def calcMoves(val, layout):
    d = {}
    d[0] = [1, 3, 4]
    d[1] = [0, 2, 3, 4, 5]
    d[2] = [1, 4, 5]
    d[3] = [0, 1, 4, 6, 7]
    d[5] = [1, 2, 4, 7, 8]
    d[6] = [3, 4, 7]
    d[7] = [3, 4, 5, 6, 8]
    d[8] = [4, 5, 7]

    l = list(layout)
    print(l)
    cur = l.index(val[0])
    val = val[1:]
    moves = 0
    for v in val:
        pos = l.index(v)
        if pos != cur:
            if pos == 4 or cur in d[pos]:
                moves += 1
            else:
                moves += 2
        cur = pos
    return moves


if __name__ == "__main__":
    print(calcMoves("44596", "923857614"))
