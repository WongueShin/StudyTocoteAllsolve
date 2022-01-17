import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    inputList = [int(input()) for _ in range(n)]
    total = sum(inputList)
    max = 0
    istie = 0
    for idx in range(n):
        if inputList[idx] > inputList[max]:
            max = idx
            istie = 1
            continue
        if inputList[idx] == inputList[max]:
            istie += 1
    if istie > 1:
        return "no winner"
    
    if inputList[max] > total//2:
        return f'majority winner {max + 1}'
    
    return f"minority winner {max + 1}"
    

T = int(input())
for _ in range(T):
    print(solution())