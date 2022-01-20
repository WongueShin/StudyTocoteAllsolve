from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
ax, ay = map(int, input().split())
m = int(input())
g = [[] for _ in range(n+1)]
visited = [0]*(n+1)

def bfs(v):
  dq = deque()
  dq.append(v)
  visited[v] = 0
  while dq:
    v = dq.popleft()
    for nv in g[v]:
      if visited[nv]==0:
        visited[nv]=visited[v]+1
        dq.append(nv)

for _ in range(m):
  x, y = map(int, input().split())
  g[x].append(y)
  g[y].append(x)

bfs(ax)

if visited[ay] != 0:
  print(visited[ay])
else:
  print(-1)