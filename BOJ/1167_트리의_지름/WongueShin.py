from sys import stdin
from collections import deque


def BFS(que, graph):
    md_node = 0
    md = 0
    result = {}
    while len(que) > 0:
        current_node = que.popleft()
        current_cost = que.popleft()
        if current_node not in result:
            result[current_node] = current_cost
            if current_cost > md:
                md = current_cost
                md_node = current_node
            for idx in range(0, len(graph[current_node]), 2):
                que += [graph[current_node][idx], graph[current_node][idx + 1] + current_cost]
    return md, md_node


def sol():
    V = int(stdin.readline())
    graph = {}
    node_list = []
    for i in range(V):
        input_list = list(map(int, stdin.readline().split()))
        node = input_list[0]
        node_list.append(node)
        graph[node] = []
        link_list = input_list[1:-1]
        graph[node] += link_list
    que = deque()
    for node in node_list:
        if len(graph[node]) >= 2:
            que += [node, 0]
            break

    fst_max_distance, fst_node = BFS(que, graph)
    que = deque([fst_node, 0])
    sec_max_distance, sec_node = BFS(que, graph)
    print(sec_max_distance)
    return


sol()