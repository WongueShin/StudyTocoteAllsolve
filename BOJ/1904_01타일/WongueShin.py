from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    memo = [-1] * (N + 2)
    memo[1] = 1
    memo[2] = 2
    for i in range(3, N + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 15746
    print(memo[N])

solution()
