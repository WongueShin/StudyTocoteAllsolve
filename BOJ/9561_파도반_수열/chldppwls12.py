from sys import stdin
input = stdin.readline

t = int(input())

def solution():
  n = int(input())
  memo = [1, 1, 1, 2, 2]
  for i in range(5, n):
    memo.append(memo[i-1] + memo[i-5])

  return memo[n-1]

for _ in range(t):
  print(solution())