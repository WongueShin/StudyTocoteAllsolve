from sys import stdin

def input():
    return stdin.readline().rstrip()


def solution():

    N = int(input())
    K = int(input())

    target = K
    start = 1
    end = N**2

    while True:
        if start > end:
            print(start)
            return

        mid = (start + end) // 2

        cnt = 0
        for i in range(1, N+1):
            cnt += min(mid//i, N)

        if cnt >= target:
            end = mid-1
        else:
            start = mid+1


solution()