import sys

def input():
    return sys.stdin.readline()

def solution():
    N = int(input().rstrip())
    inputList = list(map(int, input().rstrip().split(' ')))
    inputList.sort()
    return inputList[(N - 1)//2]

print(solution())