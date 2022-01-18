from sys import stdin
input = stdin.readline

def solution():
  n = int(input())
  vl = [int(input()) for _ in range(n)]

  ds = sum(vl) / 2
  ms = max(vl)

  maxl = [i for i, value in enumerate(vl) if value == ms]

  if len(maxl) >= 2:
    print("no winner")
  elif ms > ds:
    print(f"majority winner {vl.index(ms) + 1}")
  elif ms <= ds:
    print(f"minority winner {vl.index(ms) + 1}")

tc = int(input())
for _ in range(tc):
  solution()