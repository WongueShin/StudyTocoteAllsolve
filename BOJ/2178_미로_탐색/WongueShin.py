from collections import deque
from sys import stdin
def input():
    return stdin.readline().rstrip()

def solution():
    N, M = map(int, input().split(' '))
    mat = [list(map(int, list(input()))) for _ in range(N)]
    moveable = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    def dfs():
        que = deque([(0, 0)])
        visitDict = {(0,0): 1}
        while len(que) > 0:
            cx, cy = que.popleft()
            for case in moveable:
                dx, dy = cx + case[0], cy + case[1]
                if dx < 0 or M <= dx or dy < 0 or N <= dy:
                    continue
                if mat[dy][dx] == 0:
                    continue
                if (dx, dy) not in visitDict:
                    visitDict[(dx, dy)] = visitDict[(cx, cy)] + 1
                    que.append((dx, dy))
                    if dx == M - 1 and dy == N -1:
                        return visitDict[(cx, cy)] + 1
                    continue
                if visitDict[(dx, dy)] > visitDict[(cx, cy)] + 1:
                    visitDict[(dx, dy)] = visitDict[(cx, cy)] + 1
                    que.append((dx, dy))
                    continue
    return dfs()


print(solution())