from sys import stdin
from math import factorial

def input():
    return stdin.readline().rstrip()

def solution():
    N, M = map(int, input().split(' '))
    print(factorial(M) // ( factorial(N) * factorial(M - N)))

T = int(input())

for _ in range(T):
    solution()