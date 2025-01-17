from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    n = int(input())
    w = [0]
    for i in range(n):
        w.append(int(input()))
    dp = [0, w[1]]
    if n > 1:
        dp.append(w[1] + w[2])
    for i in range(3, n + 1):
        dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
    print(dp[n])

solution()