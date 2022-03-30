from sys import stdin
input = stdin.readline

n = int(input())
nl = [int(input()) for _ in range(n)]

memo = [0] * (max(nl)+1)
memo[1] = 1
memo[2] = 2
memo[3] = 4

def solution():
  for i in range(4, max(nl)+1):
    memo[i] = memo[i-3] + memo[i-2] + memo[i-1]

  for nn in nl:
    print(memo[nn])

solution()