from sys import stdin
input = stdin.readline

n = int(input())

def solution():
  memo = [0] * (n+2)
  memo[1] = 1
  memo[2] = 2

  for i in range(3, n+1):
    memo[i] = (memo[i-1] + memo[i-2])%15746

  return memo[n]

print(solution())