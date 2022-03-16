# 메모리 최적화
import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    MAX_NUMBER = 10001
    inputList = [0] * MAX_NUMBER
    for _ in range(N):
        inputList[int(input())] += 1
    for i in range(MAX_NUMBER):
        if inputList[i] != 0:
            for j in range(inputList[i]):
                print(i)

solution()