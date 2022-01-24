from collections import deque
from sys import stdin
input = stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

R, C = map(int, input().split())
g = [list(input()) for _ in range(R)]

visited = [[set() for _ in range(C)] for _ in range(R)]

dq = deque()
visited[0][0].add(g[0][0])
dq.append((0, 0, g[0][0]))

ans = 0

while dq:
  x, y, a = dq.popleft()
  ans = max(ans, len(a))
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<R and 0<=ny<C and g[nx][ny] not in a:
      na = a + g[nx][ny]
      if na not in visited[nx][ny]:
        visited[nx][ny].add(na)
        dq.append((nx, ny, na))

print(ans)