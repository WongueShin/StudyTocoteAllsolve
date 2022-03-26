from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
ll = list(map(int, input().split()))

def solution():
  ans = []
  for l in ll:
    if len(ans) <= bisect_left(ans, l):
      ans.append(l)
    else:
      ans[bisect_left(ans, l)] = l
    
  return len(ans)

print(solution())