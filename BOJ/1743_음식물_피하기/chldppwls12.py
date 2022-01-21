import sys
sys.setrecursionlimit(10**6)
from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
g = [['.']*M for _ in range(N)]
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

for _ in range(K):
  x, y = map(int, input().split())
  g[x-1][y-1] = '#'

visited = [[0]*M for _ in range(N)]
ans = 0
s = 0

def dfs(x, y):
  global ans, s
  visited[x][y] = 1
  s += 1
  ans = max(ans, s)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and g[nx][ny]=='#':
      dfs(nx, ny)


for i in range(N):
  for j in range(M):
    if visited[i][j]==0 and g[i][j]=='#':
      s = 0
      dfs(i, j)

print(ans)