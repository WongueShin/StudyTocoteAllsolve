from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    inputList = list(map(int, input().split(' ')))
    memo = [0] * N
    for i in range(N):
        for j in range(i):
            if inputList[i] > inputList[j] and memo[i] < memo[j]:
                memo[i] = memo[j]
        memo[i] += 1
    print(max(memo))

solution()