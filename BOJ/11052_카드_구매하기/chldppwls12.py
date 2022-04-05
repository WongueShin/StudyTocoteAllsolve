from sys import stdin
input = stdin.readline

n = int(input())
l = [0] + list(map(int, input().split()))

def solution():
  memo = [0] * (n+1)
  memo[1] = l[1]

  for i in range(2, n+1):
    for j in range(1, i+1):
      memo[i] = max(memo[i], memo[i-j]+l[j])

  return memo[n]

print(solution())