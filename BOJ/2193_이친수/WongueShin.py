from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    memo = [1,1]
    for _ in range(N - 2):
        memo.append(memo[-1] + memo[-2])
    print(memo[-1])

solution()

            