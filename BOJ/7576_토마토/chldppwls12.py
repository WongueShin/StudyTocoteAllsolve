from collections import deque
from sys import stdin
input = stdin.readline

M, N = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]

dq = deque()
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
visited = [[0] * M for _ in range(N)]

def bfs():
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<M and g[nx][ny]==0:
        g[nx][ny] = g[x][y]+1
        dq.append((nx, ny))

def solution():
  for i in range(N):
    for j in range(M):
      if g[i][j] == 1:
        dq.append((i, j))

  bfs()

  for i in range(N):
    for j in range(M):
      if g[i][j] == 0:
        return -1
      else:
        return max(map(max, g))-1

print(solution())