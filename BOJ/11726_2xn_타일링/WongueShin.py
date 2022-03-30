import sys
sys.setrecursionlimit(2000)

def input():
    return sys.stdin.readline().rstrip()

def sol():
    n = int(input())
    global memo
    memo = {0: 0, 1: 1, 2: 2}
    print(cal(n) % 10007)


def cal(n):
    global memo
    if n in memo:
        return memo[n]
    else:
        memo[n] = cal(n - 1) + cal(n - 2)
        return memo[n]

sol()