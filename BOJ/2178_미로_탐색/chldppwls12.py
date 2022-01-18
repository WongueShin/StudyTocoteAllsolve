from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
g = [list(map(int, input().rstrip())) for _ in range(N)]

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

visited = [[0] * M for _ in range(N)]

def bfs(x, y):
  dq = deque()
  dq.append((x, y))
  visited[x][y] = 1
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and g[nx][ny]==1:
        visited[nx][ny] = visited[x][y] + 1
        dq.append((nx, ny))

bfs(0, 0)

print(visited[N-1][M-1])