from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    inputList = [0] + list(map(int, input().split(' ')))
    memo = [0] * (N + 1)
    memo[1] = inputList[1]
    for i in range(2, N + 1):
        for j in range(1 , i + 1):
            if memo[i] < memo[i - j] + inputList[j]:
                memo[i] = memo[i - j] + inputList[j]
    print(memo[-1])

solution()
