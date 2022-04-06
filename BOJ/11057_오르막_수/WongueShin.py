from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    n = int(input())

    memo = list([[1] * 10])

    for _ in range(n):
        memo.append(list([0] * 10))

    for i in range(1,n+1):
        for j in range(0,10):
            for col in range(j+1):
                memo[i][j] += memo[i-1][col]

    print(memo[n][9] % 10007)

solution()