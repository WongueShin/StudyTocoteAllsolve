from collections import deque
from sys import stdin
input = stdin.readline

n, m, v = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  x, y = map(int, input().split())
  g[x][y] = g[y][x] = 1

def dfs(v):
  print(v, end=' ')
  visited[v] = 1
  for i in range(1, n+1):
    if visited[i] == 0 and g[v][i] == 1:
      dfs(i)

def bfs(v):
  dq = deque([v])
  visited[v] = 1
  while dq:
    v = dq[0]
    print(v, end=' ')
    dq.popleft()
    for i in range(1, n+1):
      if visited[i] == 0 and g[v][i] == 1:
        dq.append(i)
        visited[i] = 1

dfs(v)
print()
visited = [0] * (n+1)
bfs(v)