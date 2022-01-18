from collections import deque
from sys import stdin
input = stdin.readline

dx = (-1, 0, 1, 0, 1, -1, -1, 1)
dy = (0, 1, 0, -1, -1, 1, -1, 1)

def bfs(x, y):
  dq = deque()
  dq.append((x,y))
  visited[x][y] = 1
  while dq:
    x, y = dq.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<h and 0<=ny<w and visited[nx][ny] == 0 and g[nx][ny] == 1:
        visited[nx][ny] = 1
        dq.append((nx, ny))


while True:
  ans = 0
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  g = [list(map(int, input().split())) for _ in range(h)]
  visited = [[0]*w for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if visited[i][j] == 0 and g[i][j] == 1:
        ans += 1
        bfs(i, j)
  print(ans)