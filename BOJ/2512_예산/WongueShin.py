from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    reqList = list(map(int, input().split(' ')))
    total = int(input())
    start, end = 1, max(reqList)

    while True:
        temp = 0
        mid = (start + end) // 2
        for ele in reqList:
            if ele > mid:
                temp += mid
                continue
            temp += ele
        if start > end:
            print(end)
            return
        if temp <= total:
            start = mid + 1
            continue
        end = mid - 1
        
solution()