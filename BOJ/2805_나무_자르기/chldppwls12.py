from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
tl = list(map(int, input().split()))

def solution():
  ans = 0
  left = 1
  right = max(tl)

  while left <= right:
    mid = (left+right)//2
    s = 0
    for t in tl:
      if t > mid:
        s += t- mid
      if s >= M:
        break
    
    if s >= M:
      ans = mid
      left = mid+1
    else:
      right = mid-1

  return ans

print(solution())