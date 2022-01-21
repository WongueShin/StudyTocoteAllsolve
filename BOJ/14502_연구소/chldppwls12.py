from collections import deque
from itertools import combinations
from sys import stdin
input = stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
blank = []
wall = []
virus = []

def dfs(x, y):
  visited[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and g[nx][ny]==0:
      g[nx][ny] = 2
      dfs(nx, ny)

for i in range(N):
  for j in range(M):
    if g[i][j]==0:
      blank.append((i, j))
    elif g[i][j]==1:
      wall.append((i, j))
    elif g[i][j]==2:
      virus.append((i, j))

ans = []
for c in list(combinations(blank, 3)):
  visited = [[0]*M for _ in range(N)]
  cnt = 0
  for x, y in c:
    g[x][y] = 1
  for i in range(N):
    for j in range(M):
      if visited[i][j]==0 and g[i][j]==2:
        dfs(i, j)

  for i in range(N):
    for j in range(M):
      if g[i][j]==0:
        cnt +=1

  ans.append(cnt)

  for i in range(N):
    for j in range(M):
      g[i][j] = 0
  
  for x, y in wall:
    g[x][y] = 1
  
  for x, y in virus:
    g[x][y] = 2

print(max(ans))