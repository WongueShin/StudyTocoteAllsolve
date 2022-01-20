from sys import stdin
from collections import deque
def input():
    return stdin.readline().rstrip()

def solution(w, h):
    maplist = [list(map(int, input().split(' '))) for _ in range(h)]
    moveable = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    def search(x, y):
        que = deque([(x, y)])
        while len(que) > 0:
            cx, cy = que.popleft()
            for case in moveable:
                dx, dy = cx + case[0], cy + case[1]
                if w <= dx or dx < 0 or h <= dy or dy < 0:
                    continue
                if maplist[dy][dx] == 1:
                    que.append((dx, dy))
                    maplist[dy][dx] = 0
    conter = 0
    for j in range(h):
        for i in range(w):
            if maplist[j][i] == 1:
                conter += 1
                search(i, j)
    return conter


while True:
    w, h = map(int, input().split(' '))
    if w == h == 0:
        break
    print(solution(w, h))