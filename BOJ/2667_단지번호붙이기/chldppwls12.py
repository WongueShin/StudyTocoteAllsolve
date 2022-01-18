from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
g = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def bfs(x, y):
  cnt = 0
  visited[x][y] = 1
  dq = deque()
  dq.append((x, y))
  while dq:
    x, y = dq.popleft()
    cnt+=1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<N and g[nx][ny]==1 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        dq.append((nx, ny))
  return cnt

for i in range(N):
  for j in range(N):
    if g[i][j] == 1 and visited[i][j] == 0:
      ans.append(bfs(i, j))

print(len(ans))
for a in sorted(ans):
  print(a)