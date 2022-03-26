from bisect import bisect
from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N, M = map(int, input().split(' '))
    A = sorted(list(map(int, input().split(' '))))
    B = sorted(list(map(int, input().split(' '))))
    count = 0
    for ele in A:
        count += bisect(B, ele - 1)
    print(count)


T = int(input())
for _ in range(T):
    solution()