import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    graph = {i: [] for i in range(1, n+1)}
    start, end = map(int, input().split(' '))
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split(' '))
        graph[x].append(y)
        graph[y].append(x)

    def bfs():
        queue = deque([start])
        visit = [-1 for _ in range(n)]
        visit[start - 1] = 0
        while len(queue) > 0:
            currentNode = queue.popleft()
            nodeList = graph[currentNode]
            for node in nodeList:
                if visit[node - 1] == -1:
                    visit[node - 1] = visit[currentNode - 1] + 1
                    queue.append(node)
                    continue
                if visit[node - 1] > visit[currentNode - 1] + 1:
                    visit[node - 1] = visit[currentNode - 1] + 1
                    queue.append(node)
        return visit

    return bfs()[end - 1]
    
print(solution())