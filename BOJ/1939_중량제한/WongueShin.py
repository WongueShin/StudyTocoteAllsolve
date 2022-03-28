from collections import deque
from sys import stdin

def input():
    return stdin.readline().rstrip()

def bfs(start, mid, end, graph, visit):
        visit[start] = 1
        q = deque()
        q.append(start)
        while q:
            start = q.popleft()
            if start == end: return True
            for nx, nc in graph[start]:
                if visit[nx] == 0 and mid <= nc:
                    q.append(nx)
                    visit[nx] = 1
        return False

def solution():
    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    for i in range(M):
        node01, node02, weigh = map(int, input().split())
        graph[node01].append([node02, weigh])
        graph[node02].append([node01, weigh])
    start, end = map(int, input().split())
    low, high = 1, 1000000000

    while low <= high:
        visit = [0 for i in range(N + 1)]
        mid = (low + high) // 2
        if bfs(start, mid, end, graph, visit): low = mid + 1
        else: high = mid - 1
    print(high)

solution()