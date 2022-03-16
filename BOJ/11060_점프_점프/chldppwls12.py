from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
a = list(map(int, input().split()))

visited = [0] * N
ans = 0

if N == 1:
  ans = 0
else:
  dq = deque()
  dq.append(0)
  while dq:
    x = dq.popleft()
    jump = a[x]
    for i in range(1, jump+1):
      if x+i < N and visited[x+i] == 0:
        visited[x+i] = visited[x] + 1
        dq.append(x+i)

  if visited[N-1] == 0:
    ans = -1
  else:
    ans = max(visited)

print(ans)