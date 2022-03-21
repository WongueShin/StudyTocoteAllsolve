from sys import stdin
input = stdin.readline
#from bisect import bisect_left, bisect_right

T = int(input())

def solution():
  N = int(input())
  nl = list(map(int, input().split()))
  M = int(input())
  ml = list(map(int, input().split()))

  set_nl = set(nl)

  for m in ml:
    if m in set_nl:
      print(1)
    else:
      print(0)

  # nl.sort()
  # for i in ml:
  #   if bisect_left(nl, i) == bisect_right(nl, i):
  #     print(0)
  #   else:
  #     print(1)

for _ in range(T):
  solution()