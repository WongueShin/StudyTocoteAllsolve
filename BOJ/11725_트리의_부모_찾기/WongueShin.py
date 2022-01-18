import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def bfs_searching(graph):
    stack = deque()
    visit = {}
    memo = {1: None}
    for node in graph[1]:
        stack.append(node)
        memo[node] = 1
    while len(stack) > 0:
        searching_node = stack.popleft()
        if searching_node in visit:
            continue
        visit[searching_node] = True
        for node in graph[searching_node]:
            if node not in memo:
                memo[node] = searching_node
            if node in visit:
                continue
            stack.append(node)
    return memo

def solution():
    number_of_nodes = int(input())
    graph = {1: []}

    for connection in range(number_of_nodes - 1):
        node01, node02 = list(map(int, input().split()))
        if node01 not in graph:
            graph[node01] = []
        if node02 not in graph:
            graph[node02] = []
        graph[node01].append(node02)
        graph[node02].append(node01)


    parent_node = bfs_searching(graph)

    for i in range(2, number_of_nodes + 1):
        print(parent_node[i])
    
solution()