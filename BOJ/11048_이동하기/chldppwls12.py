from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

def solution():
  l = [list(map(int, input().split())) for _ in range(n)]
  memo = [[0] * (m+1) for _ in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, m+1):
      memo[i][j] = l[i-1][j-1] + max(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])

  return memo[n][m]

print(solution())