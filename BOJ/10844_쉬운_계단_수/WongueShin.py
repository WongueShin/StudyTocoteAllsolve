from sys import stdin

def input():
    return stdin.readline().strip()

def solution():
    N = int(input())
    cache = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for _ in range(N - 1):
        temp = [0]*10
        for n in range(10):
            if n-1 >= 0:
                temp[n-1] += cache[n]
            if n+1 <= 9:
                temp[n+1] += cache[n]
        cache = temp
    print(sum(cache) % 1000000000)

solution()