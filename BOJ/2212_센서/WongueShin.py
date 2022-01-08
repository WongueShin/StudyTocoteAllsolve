import sys

def input():
    return sys.stdin.readline()


def solution():
    N = int(input().rstrip())
    K = int(input().rstrip())
    inputList = list(map(int, input().rstrip().split(' ')))
    inputList.sort()
    distList = [inputList[i] - inputList[i -1] for i in range(1, N)]
    distList.sort(reverse=True)
    distList = distList[K - 1:]
    return sum(distList)


print(solution())
