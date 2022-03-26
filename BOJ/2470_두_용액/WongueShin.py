from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    inputList = sorted(list(map(int, input().split(' '))))
    left, right = 0, N - 1
    ans = inputList[0] + inputList[-1]
    al, ar = 0, -1

    while True:
        if left >= right:
            break
        temp = inputList[left] + inputList[right]
        if abs(temp) < abs(ans):
            ans = temp
            al = left
            ar = right
        if ans == 0:
            break
        if temp < 0:
            left += 1
            continue
        right -= 1

    print(inputList[al], inputList[ar])
    
solution()
        