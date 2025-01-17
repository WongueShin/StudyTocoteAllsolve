from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N, M = map(int, input().split())
    memo = [[0] * (M + 1)] * (N + 1)
    candy = []

    for i in range(N):
        candy.append(list(map(int, input().split())))

    for i in range(1, N+1):
        for j in range(1, M+1):
            memo[i][j] = max(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]) + candy[i-1][j-1]

    print(memo[N][M])

solution()