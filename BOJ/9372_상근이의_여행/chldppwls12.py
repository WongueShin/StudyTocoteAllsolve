from sys import stdin
input = stdin.readline

T = int(input())

def dfs(v, cnt):
  visited[v] = 1
  for i in g[v]:
    if visited[i] == 0:
      cnt = dfs(i, cnt+1)
  
  return cnt

for _ in range(T):
  N, M = map(int, input().split())
  g = [[] for _ in range(N+1)]
  visited = [0] *(N+1)
  
  for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

  print(dfs(1, 0))