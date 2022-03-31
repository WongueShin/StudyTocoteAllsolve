from sys import stdin
input = stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

def solution():
  memo = [0, l[1], l[1]+l[2]]

  for i in range(3, n+1):
    memo.append(max(memo[i-1], memo[i-3]+l[i-1]+l[i], memo[i-2]+l[i]))

print(solution())