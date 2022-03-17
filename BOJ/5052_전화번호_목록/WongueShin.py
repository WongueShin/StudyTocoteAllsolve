import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    inputList = [input() for _ in range(n)]
    inputList.sort()
    for i in range(n -1):
        if inputList[i] in inputList[i + 1][0:len(inputList[i])]:
            return 'NO'
    return 'YES'

t = int(input())
for _ in range(t):
    print(solution())