from collections import deque
from sys import stdin
input = stdin.readline

def solution():
  n, m = map(int, input().split())
  dq = deque(map(int, input().split()))
  idx_dq = deque(i for i in range(n))
  cnt = 0
  while len(dq) > 0:
    if dq[0] == max(dq):
      cnt += 1
      dq.popleft()
      if idx_dq.popleft() == m:
        return cnt
      continue
    dq.append(dq.popleft())
    idx_dq.append(idx_dq.popleft())
  

t = int(input())

for _ in range(t):
  print(solution())