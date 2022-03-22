import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N, K = map(int, input().split(' '))
    inputList = sorted(list(map(int, input().split(' '))))
    print(inputList[K - 1])

solution()