from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    n = int(input())
    inputList = list(map(int, input().split(' ')))
    memo = [inputList[0]]
    for i in range(n - 1):
        memo.append(max(memo[i] + inputList[i + 1], inputList[i + 1]))
    print(max(memo))

solution()