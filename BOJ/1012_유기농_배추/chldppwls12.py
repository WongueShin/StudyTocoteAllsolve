from collections import deque
from sys import stdin
input = stdin.readline

T = int(input())

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def bfs(y, x):
  dq = deque()
  dq.append((y, x))
  while dq:
    y, x = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<M and 0<=ny<N and g[ny][nx] == 1:
        g[ny][nx] = 0
        dq.append((ny, nx))


for _ in range(T):
  M, N, K = map(int, input().split())
  cnt = 0
  g = [[0] * M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    g[y][x] = 1
  
  for i in range(N):
    for j in range(M):
      if g[i][j] == 1:
        g[i][j] = 0
        bfs(i, j)
        cnt += 1
  
  print(cnt)