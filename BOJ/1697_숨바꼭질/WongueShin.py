import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def solution():
    N, K = map(int, input().split(' '))

    size_of_space = max(N, K)
    size_of_space = size_of_space + (size_of_space // 2) + 2
    if N == K:
        return 0
    space = [0 for _ in range(1, size_of_space)]
    que = deque([[N]])
    times = 0
    while True:
        times += 1
        current = que.pop()
        travable = []
        for node in current:
            if node - 1 == K or node + 1 == K or node * 2 == K:
                return times
            if node - 1 >= 0:
                if space[node - 2] == 0 or space[node - 2] > times:
                    space[node - 2] = times
                    travable.append(node - 1)
            if node + 1 < size_of_space:
                if space[node] == 0 or space[node] > times:
                    space[node] = times
                    travable.append(node + 1)
            if node * 2 < size_of_space:
                if space[(node * 2) - 1] == 0 or space[(node * 2) - 1] > times:
                    space[(node * 2) - 1] = times
                    travable.append(node * 2)
        que.append(travable)

print(solution())