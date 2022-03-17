from sys import stdin
from collections import deque
input = stdin.readline

N, M, K, X = map(int, input().split())
g = [[] for _ in range(N+1)]
ans = []
visited = [-1] * (N+1)
for _ in range(M):
  a, b = map(int, input().split())
  g[a].append(b)

dq = deque()
dq.append(X)
visited[X] = 0
while dq:
  x = dq.popleft()
  for i in g[x]:
    if visited[i] == -1:
      visited[i] = visited[x] + 1
      dq.append(i)
      if visited[i] == K:
        ans.append(i)

if len(ans) == 0:
  print(-1)
else:
  for a in sorted(ans):
    print(a)