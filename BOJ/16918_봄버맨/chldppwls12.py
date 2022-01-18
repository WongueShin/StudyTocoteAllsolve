from sys import stdin
input = stdin.readline

R, C, N = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

tl = [[0] * C for _ in range(R)]

for i in range(R):
  for j in range(C):
    if m[i][j] == 'O':
      tl[i][j] = 3

#폭탄 설치
def install(time):
  for i in range(R):
    for j in range(C):
      if m[i][j] == '.':
        m[i][j] = 'O'
        tl[i][j] = time + 3

#폭탄 터짐
def boom(time):
  for i in range(R):
    for j in range(C):
      if tl[i][j] == time:
        for d in range(4):
          nx = i + dx[d]
          ny = j + dy[d]
          if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
          if m[nx][ny] == '.':
            continue
          m[nx][ny] = '.'
        m[i][j] = '.'
        tl[i][j] = 0

time = 2

while time <= N:
  if time % 2 == 0:
    install(time)
  elif time % 2 == 1:
    boom(time)
  time += 1

for i in range(R):
  for j in range(len(m[i])):
    print(m[i][j], end='')
  print()