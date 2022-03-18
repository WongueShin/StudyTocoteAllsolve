import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    inputList = sorted(list(map(int,input().split(' '))))
    x = int(input())
    answer = 0
    left, right = 0, n-1
    while left < right:
        temp = inputList[left] + inputList[right]
        if temp == x:
            answer += 1
            left += 1
        elif temp < x:
            left += 1
        else:
            right -= 1
    print(answer)
        

solution()