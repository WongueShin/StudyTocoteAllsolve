import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def bfs(que, graph, check_list):
    while len(que) > 0:
        current_node = que[0]
        link_list = graph[current_node]
        for linked_node in link_list:
            if not check_list[linked_node]:
                check_list[linked_node] = True
                que.append(linked_node)
        que.popleft()

def solution():
    N, M = map(int, input().split())

    check_list = [True] + [False] * N
    graph = {}
    for i in range(1, N + 1):
        graph[i] = [i]

    for j in range(M):
        node01, node02 = map(int, input().split())
        graph[node01].append(node02)
        graph[node02].append(node01)
    num_of_cc = 0
    while False in check_list:
        que = deque()
        que.append(check_list.index(False))
        bfs(que, graph, check_list)
        num_of_cc += 1
    return num_of_cc


print(solution())