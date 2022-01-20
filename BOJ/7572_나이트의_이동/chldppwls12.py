from collections import deque
from sys import stdin
input = stdin.readline

dx = (-1, 1, -2, 2, -2, 2, -1, 1)
dy = (-2, -2, -1, -1, 1, 1, 2, 2)
def bfs(x, y):
  cnt = 0
  dq = deque()
  dq.append((x, y, cnt))
  visited[x][y] = 1
  while dq:
    x, y, cnt = dq.popleft()
    if x == gox and y == goy:
      return cnt
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<I and 0<=ny<I and visited[nx][ny]==0:
        visited[nx][ny] = 1
        dq.append((nx, ny, cnt+1))
  return cnt


tc = int(input())
for _ in range(tc):
  I = int(input())
  visited = [[0]*I for _ in range(I)]
  curx, cury = map(int, input().split())
  gox, goy = map(int, input().split())

  if curx == gox and cury == goy:
    print(0)
    continue

  print(bfs(curx, cury))