from sys import stdin
input = stdin.readline

X, Y = map(int, input().split())

def solution():
  r = Y* 100//X
  if r >= 99:
    return -1
  else:
    ans = 0
    left = 1
    right = 1000000000

    while left <= right:
      mid = (left+right)//2
      nx, ny = X+mid, Y+mid
      if ny*100//nx <= r:
        left = mid+1
      else:
        ans = mid
        right = mid-1
  
  return ans

print(solution())