from sys import stdin
input = stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

def solution():
  memo = [0] * (n+1)
  for i in range(n-1, -1, -1):
    if i + l[i][0] > n:
      memo[i] = memo[i-1]
    else:
      memo[i] = max(l[i][1] + memo[i+l[i][0]], memo[i+1])

  return memo[0]

print(solution())