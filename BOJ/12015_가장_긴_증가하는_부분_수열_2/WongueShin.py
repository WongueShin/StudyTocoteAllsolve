from sys import stdin
from bisect import bisect_left
# len이 관심사이므로 bisect로 풀이 가능하다. (기억해두는게 좋을꺼 같음)

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    inputList = list(map(int, input().split(' ')))
    stack = [0]
    
    for ele in inputList:
        if stack[-1] < ele:
            stack.append(ele)
            continue
        stack[bisect_left(stack, ele)] = ele
    
    print(len(stack) - 1)

solution()