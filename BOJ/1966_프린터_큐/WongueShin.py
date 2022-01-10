import sys
from collections import deque

def input():
    return sys.stdin.readline()

def solution():
    N, M = map(int, input().rstrip().split(' '))
    inputList =  list(map(int, input().rstrip().split(' ')))
    queue = deque()
    for idx in range(N):
        queue.append((idx, inputList[idx]))
    result = []
    while len(queue) > 0:
        priority = queue[0][1]
        condition = False
        for ele in queue:
            if priority < ele[1]:
                condition = True
                break
        if condition:
            queue.append(queue.popleft())
            continue
        result.append(queue.popleft())
    
    return result.index((M,inputList[M])) + 1


T = int(input().rstrip())

for _ in range(T):
    print(solution())