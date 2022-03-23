from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N, M = map(int, input().split(' '))
    treeList = list(map(int, input().split(' ')))
    start, end = 1, max(treeList)
    
    while True:
        if start > end:
            print(end)
            return
        mid = (start + end) // 2
        temp = 0
        for ele in treeList:
            if ele >= mid:
                temp += ele - mid
        if temp >= M:
            start = mid + 1
            continue
        end = mid - 1

solution()