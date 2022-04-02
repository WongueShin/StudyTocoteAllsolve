from sys import stdin
input = stdin.readline

n = int(input())

def solution():
  memo = [0, 1, 1]
  for i in range(3, n+1):
    memo.append(memo[i-2] + memo[i-1])

  return memo[n]

print(solution())