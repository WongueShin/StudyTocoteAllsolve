from sys import stdin
input = stdin.readline

n = int(input())

memo = [0]*1001
memo[1] = 1
memo[2] = 2

def solution():
  for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2]
  
  return memo[n]%10007

print(solution())