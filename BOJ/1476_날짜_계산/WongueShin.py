import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    #E = 1 ~ 15 S = 1 ~ 28 M = 1 ~ 19
    E, S, M = map(int, input().split(' '))
    if E == S == M:
        return E
    counter = 1
    temp = [1, 1, 1]
    while temp != [E, S, M]:
        counter += 1
        temp = [temp[0]+1, temp[1]+1, temp[2]+1]
        if temp[0] > 15:
            temp[0] = 1
        if temp[1] > 28:
            temp[1] = 1
        if temp[2] > 19:
            temp[2] = 1 
    return counter

print(solution())

"""
이게.... 되네?

"""