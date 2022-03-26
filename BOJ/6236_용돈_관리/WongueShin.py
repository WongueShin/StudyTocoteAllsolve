from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N, M = map(int, input().split(' '))
    inputList = [int(input()) for _ in range(N)]

    start = min(inputList)
    end = sum(inputList)

    ans = 0
    while True:
        if start > end:
            print(ans)
            return

        mid = (start + end) // 2
        wallet = 0
        cnt = 0
        for ele in inputList:
            if wallet < ele:
                wallet = mid
                cnt += 1
            wallet -= ele
        
        if cnt > M or mid < max(inputList):
            start = mid + 1
            continue
        end = mid - 1
        ans = mid
        
solution()