from sys import stdin
#from math import factorial
input = stdin.readline

t = int(input())

# def solution():
#   n, m = map(int, input().split())
#   cnt = factorial(m) // (factorial(n) * factorial(m-n))
#   return cnt

def solution():
  n, m = map(int, input().split())
  memo = [[0]*30 for _ in range(30)]

  for i in range(30):
    for j in range(30):
      if i == 1:
        memo[i][j] = j
      else:
        if i == j:
          memo[i][j] = 1
        elif i < j:
          memo[i][j] = memo[i-1][j-1] + memo[i][j-1]

  return memo[n][m]

for _ in range(t):
  print(solution())