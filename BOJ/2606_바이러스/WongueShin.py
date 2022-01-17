import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def search_connected_computer(input_graph): 
    visit = {}
    stack = deque()

    for i in graph[1]:
        stack.append(i)

    number_of_connected_computer = -1
    while len(stack) > 0:
        current_node = stack.popleft()

        if current_node in visit:
            continue

        visit[current_node] = True

        number_of_connected_computer += 1
        connected_list = graph[current_node]

        for connected_node in connected_list:
            if connected_node in visit:
                continue
            stack.append(connected_node)
    return number_of_connected_computer

def solution():
    Num_of_computers = int(input())
    Num_of_connection = int(input())

    graph = {}

    for i in range(1, Num_of_computers + 1):
        graph[i] = []

    for i in range(Num_of_connection):
        computer01, computer02 = list(map(int, stdin.readline().split()))
        graph[computer01].append(computer02)
        graph[computer02].append(computer01)

    num_of_com = search_connected_computer(graph)

    return num_of_com

print(solution())