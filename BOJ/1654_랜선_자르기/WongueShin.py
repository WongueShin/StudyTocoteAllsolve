from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    K, N = map(int, input().split(' '))
    inputList = [int(input()) for _ in range(K)]
    start, end = 1, max(inputList)
    while True:
        mid = (start + end) // 2
        temp = 0
        for i in inputList:
            temp += i // mid
        if start > end:
            print(end)
            return
        if temp >= N:
            start = mid + 1
            continue
        end = mid - 1

solution()