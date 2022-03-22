from sys import stdin
input = stdin.readline

n = int(input())
wl = [int(input()) for _ in range(n)]

def solution():
  ans = []
  wl.sort(reverse=True)
  for i in range(n):
    ans.append(wl[i] * (i+1))
  
  return max(ans)

print(solution())