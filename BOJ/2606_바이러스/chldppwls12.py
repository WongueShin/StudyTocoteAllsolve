from sys import stdin
input = stdin.readline

n = int(input())
cn = int(input())

g = [[0]*(n+1) for _ in range(n+1)]

for _ in range(cn):
  x, y = map(int, input().split())
  g[x][y] = g[y][x] = 1

visited= [0]*(n+1)

ans = []

def dfs(v):
  visited[v] = 1
  for i in range(1, n+1):
    if visited[i] == 0 and g[v][i] == 1:
      ans.append(i)
      dfs(i)

dfs(1)
print(len(ans))