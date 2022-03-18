from sys import stdin
input = stdin.readline

N = int(input())
l = [int(input()) for _ in range(N)]

def solution(l):
  l.sort()

  ans = 0
  for i in range(1, N+1):
    ans += abs(i - l[i-1])
  
  return ans

print(solution(l))