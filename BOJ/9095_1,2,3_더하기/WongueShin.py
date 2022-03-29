from sys import stdin

def input():
    return stdin.readline().rstrip()

def compute(n):
    if n == 3:
        return 4
    if n == 2:
        return 2
    if n == 1:
        return 1
    return compute(n - 1) + compute(n - 2) + compute(n - 3)


def sol():
    n = int(input())
    print(compute(n))


T = int(input())

for _ in range(T):
    sol()
