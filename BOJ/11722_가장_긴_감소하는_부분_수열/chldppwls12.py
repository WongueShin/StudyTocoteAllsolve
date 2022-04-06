from sys import stdin
input = stdin.readline

n = int(input())
l = list(map(int, input().split()))

def solution():
  memo = [1] * n
  for i in range(n):
    for j in range(i):
      if l[j] > l[i]:
        memo[i] = max(memo[i], memo[j]+1)

  return max(memo)

print(solution())