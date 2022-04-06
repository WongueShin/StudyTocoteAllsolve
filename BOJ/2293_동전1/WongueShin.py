from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    n, k = map(int, input().split())
    c = []
    memo = [0 for i in range(k + 1)]
    memo[0] = 1
    for i in range(n):
        c.append(int(input()))
    for i in c:
        for j in range(1, k + 1):
            if j - i >= 0:
                memo[j] += memo[j - i]
    print(memo[k])

solution()