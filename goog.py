#!/Users/pwu/anaconda/bin/python3
import math
def solution(xs):
    neg = []
    pos = []
    for v in xs:
        if v > 0:
            pos.append(v)
        elif v < 0:
            neg.append(v)
    neg.sort()
    if len(neg) % 2 != 0:
        neg = neg[:len(neg) -1]
        print(neg)
    for n in neg:
        pos.append(n)
    if len(pos) == 0:
        return "0"
    else:
        print("pos {}".format(pos))
        tot = 1
        for i in pos:
            tot *=i 
        return str(tot)

if __name__ == '__main__':
    print(solution([-2, -3, 4, -5]))
    print ('============')
    print(solution([-2, 0, 1, -1, -1]))
    print ('============')
    print(solution([-2, 2, 5, 0, 1]))
    print ('============')
    print(solution([-2, -3]))
    print ('============')
    print(solution([-2, -3, -3]))
    print ('============')
    print(solution([2, 3, 3]))
    print("----------")
    print(solution([-1000 for i in range(50)]))
    print("----------")
    print(solution([1]))
    print("----------")
    print(solution([-1]))
    print("----------")
    print(solution([-1, 2, 0]))
    print("----------")
    print(solution([-1, 0]))
