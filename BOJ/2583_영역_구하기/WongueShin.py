from collections import deque
from sys import stdin
def input():
    return stdin.readline().rstrip()

def solution():
    M, N, K = map(int, input().split(' '))
    mapList = [[0 for i in range(N)] for j in range(M)]
    for _ in range(K):
        sq = list(map(int, input().split(' ')))
        start, end = sq[0:2], sq[2:]
        for x in range(start[0], end[0]):
            for y in range(start[1], end[1]):
                if mapList[y][x] == 0:
                    mapList[y][x] = 1
    result = []

    def bfs(props):
        que = deque([props])
        surrond = ((0, 1), (0, -1), (1, 0), (-1, 0))
        counter = 0
        while len(que) > 0:
            cx, cy = que.pop()
            if mapList[cy][cx] == 2:
                continue
            counter += 1
            mapList[cy][cx] = 2
            for case in surrond:
                dx, dy = cx + case[0], cy + case[1]
                if dx < 0 or N <= dx or dy < 0 or M <= dy:
                    continue
                if mapList[dy][dx] == 0:
                    que.append((dx, dy))
        return counter


    for i in range(N):
        for j in range(M):
            if mapList[j][i] == 0:
                result.append(bfs((i, j)))
    result.sort()
    print(len(result))
    print(' '.join(list(map(str,result))))

solution()