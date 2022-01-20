from collections import deque
from sys import stdin
def input():
    return stdin.readline().rstrip()

def solution():
    def dfs():
        que = deque([start])
        while len(que) > 0:
            cx, cy = que.popleft()
            for case in moveable:
                dx, dy = cx + case[0], cy + case[1]
                if l <= dx or dx < 0 or l <= dy or dy < 0:
                    continue
                if (dx, dy) not in visitdict:
                    visitdict[(dx, dy)] = visitdict[(cx, cy)] + 1
                    que.append((dx, dy))
                    if (dx, dy) == end:
                        return visitdict[(cx, cy)] + 1
                    continue
                
                if visitdict[(dx, dy)] > visitdict[(cx, cy)] + 1:
                    visitdict[(dx, dy)] = visitdict[(cx, cy)] + 1
                    que.append((dx, dy))
        

    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    if start == end:
        return 0
    moveable = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    visitdict = {start: 0}
    return dfs() 

T = int(input())
for _ in range(T):
    print(solution())