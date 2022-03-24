from sys import stdin
import math
input = stdin.readline

n = int(input())

def solution():
  ans = 0
  left = 0
  right = int(math.sqrt(n)) + 1

  while left <= right:
    mid = (left+right)//2

    if mid**2 < n:
      left = mid+1
    elif mid**2 > n:
      ans = mid
      right = mid-1
    else:
      return mid

  return ans

print(solution())