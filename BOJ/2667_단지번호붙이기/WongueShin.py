from sys import stdin
from collections import deque
def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    maplist = [list(input()) for _ in range(N)]
    ansList = []
    counter = 0
    liked = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(props):
        que = deque([props])
        result = 0
        visit = {}
        while len(que) > 0:
            ci, cj = que.pop()
            result += 1
            maplist[cj][ci] = '0'
            for case in liked:
                di, dj = ci + case[0], cj + case[1]
                if di < 0 or N <= di or dj < 0 or N <= dj:
                    continue
                if maplist[dj][di] == '1' and (di, dj) not in visit:
                    que.append((di, dj))
                    visit[(di, dj)] =True
        return result

    for j in range(N):
        for i in range(N):
            if maplist[j][i] == '1': 
                ansList.append(bfs((i, j)))
                counter += 1
    print(counter)
    ansList.sort()
    for i in ansList:
        print(i)


solution()