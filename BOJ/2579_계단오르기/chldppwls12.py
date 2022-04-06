from sys import stdin
input = stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

def solution():
  memo = [l[0], l[0]+l[1], max(l[0]+l[2], l[1]+l[2])]

  for i in range(3, n):
    memo.append(max(memo[i-2]+l[i], memo[i-3]+l[i]+l[i-1]))

  return memo[n-1]

print(solution())