from sys import stdin
input = stdin.readline

N = int(input())
info = []

for _ in range(N):
  name, kor, eng, math = input().rstrip().split()
  info.append((name, int(kor), int(eng), int(math)))

# for _ in range(N):
#   x = input().split()
#   scr = list(map(int, x[1:]))
#   info.append([x[0], *scr])

info.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for i in info:
  print(i[0])