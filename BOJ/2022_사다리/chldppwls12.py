from sys import stdin
import math
input = stdin.readline

x, y, c = map(float, input().split())

def solution():
  left = 0
  right = min(x, y)

  while left+0.001 <= right:
    mid = (left+right)/2
    h1 = math.sqrt(x*x - mid*mid)
    h2 = math.sqrt(y*y - mid*mid)
    h = (h1*h2) / (h1+h2)
    if h > c:
      left = mid
    else:
      right = mid
  
  return mid

print("%.3f" %round(solution(), 3))