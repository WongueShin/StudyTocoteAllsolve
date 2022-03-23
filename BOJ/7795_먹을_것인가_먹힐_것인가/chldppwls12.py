from sys import stdin
from bisect import bisect_left
input = stdin.readline

T = int(input())

for _ in range(T):
  cnt = 0
  x, y = map(int, input().split())
  xl = list(map(int, input().split()))
  yl = list(map(int, input().split()))

  yl.sort()

  for xx in xl:
    cnt += bisect_left(yl, xx)

  print(cnt)