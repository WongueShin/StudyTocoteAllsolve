from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    if N <= 2:
        if N == 2:
            print(7)
            return
        if N == 1:
            print(3)
            return
        if N == 0:
            print(0)
            return
    current = 7
    former = 3
    i = 0
    while i < N - 2:
        temp = current
        current = (current * 2) + former
        former = temp
        i += 1
    print(current % 9901)
    return

solution()