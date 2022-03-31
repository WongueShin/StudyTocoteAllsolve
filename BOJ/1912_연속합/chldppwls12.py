from sys import stdin
input = stdin.readline

n = int(input())
l = list(map(int, input().split()))

def solution():
  memo = [l[0]]

  for i in range(n-1):
    memo.append(max(memo[i] + l[i+1], l[i+1]))

  return max(memo)

print(solution())