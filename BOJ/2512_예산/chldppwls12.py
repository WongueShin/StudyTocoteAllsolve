from sys import stdin
input = stdin.readline

N = int(input())
nl = list(map(int, input().split()))
M = int(input())

def solution():
  ans = 0
  left = 0
  right = max(nl)
  
  while left <= right:
    tot = 0
    mid = (left+right)//2

    for n in nl:
      if n > mid:
        tot += mid
      else:
        tot += n

    if tot <= M:
      ans = mid
      left = mid+1
    else:
      right = mid-1

  return ans

print(solution())