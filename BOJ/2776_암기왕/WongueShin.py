from sys import stdin
from bisect import bisect_left

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    memo1 = sorted(list(map(int, input().split(' '))))
    M = int(input())
    memo2 = list(map(int, input().split(' ')))
    for case in memo2:
        index = bisect_left(memo1, case)
        if index >= len(memo1) or (case != memo1[index]):
            print(0)
            continue
        print(1)

T = int(input())

for _ in range(T):
    solution()