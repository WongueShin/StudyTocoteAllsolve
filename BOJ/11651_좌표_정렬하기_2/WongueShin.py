import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    dotList = []
    for i in range(N):
        x, y = map(int, input().split(' '))
        dotList.append([y, x])
    
    dotList.sort()
    for y, x in dotList:
        print(x, y)

solution()