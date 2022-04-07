from sys import stdin
input = stdin.readline

n = int(input())

def solution():
  memo = [1]*10

  for _ in range(n-1):
    for j in range(1, 10):
      memo[j] += memo[j-1]

  return sum(memo)%10007

print(solution())