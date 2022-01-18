import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
  x, y = map(int, input().split())
  g[x].append(y)
  g[y].append(x)

def dfs(v):
  visited[v] = 1
  for i in g[v]:
    if visited[i] == 0:
      dfs(i)

cnt = 0
for i in range(1, N+1):
  if visited[i] == 0:
    dfs(i)
    cnt += 1

print(cnt)