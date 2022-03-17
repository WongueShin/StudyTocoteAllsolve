from sys import stdin
input = stdin.readline

R, C = map(int, input().split())
g = []
for _ in range(R):
  g.append(list(input().rstrip()))

ans = []

for i in range(R):
  w = ''
  for j in range(C):
    if g[i][j] == '#':
      if len(w) > 1:
        ans.append(w)
      w = ''
    else:
      w += g[i][j]
  if len(w) > 1:
    ans.append(w)

for i in range(C):
  w = ''
  for j in range(R):
    if g[j][i] == '#':
      if len(w)>1:
        ans.append(w)
      w = ''
    else:
      w += g[j][i]
  if len(w) > 1:
    ans.append(w)

print(sorted(ans)[0])