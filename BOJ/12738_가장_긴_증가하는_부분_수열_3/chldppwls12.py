from sys import stdin
from bisect import bisect_left
input = stdin.readline

n = int(input())
ll = list(map(int, input().split()))

def solution():
  ans = []
  for l in ll:
    i = bisect_left(ans , l)
    if len(ans) <= i:
      ans.append(l)
    else:
      ans[i] = l
    
  return len(ans)

print(solution())