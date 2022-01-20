from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

minh = min(map(min, g))
maxh = max(map(max, g))

def bfs(x, y, h):
  dq = deque()
  dq.append((x, y))
  visited[x][y] = 1
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and g[nx][ny]>h:
        visited[nx][ny] = 1
        dq.append((nx, ny))

ans = []
for h in range(minh-1, maxh):
  cnt = 0
  visited = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if visited[i][j]==0 and g[i][j]>h:
        bfs(i, j, h)
        cnt += 1
  ans.append(cnt)

print(max(ans))