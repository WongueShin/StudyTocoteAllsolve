import sys
def input():
    return sys.stdin.readline()

def solution():
    N, K = map(int, input().split())
    inputList = list(map(int, input().split()))
    multap = [0 for _ in range(N)]
    counter = 0
    for idx in range(K):
        case = inputList[idx]
        if case in multap:
            continue
        if 0 in multap:
            multap[multap.index(0)] = case
            continue
        counter += 1
        memo = [0 for _ in range(K + 1)] # 앞으로 다시 사용될 차례의 인덱스
        for jdx in range(idx, K):
            ele = inputList[jdx]
            memo[ele] = jdx if memo[ele] == 0 else memo[ele] 
        latest = 0
        isSwap = False
        for plugged in multap:
            if plugged not in inputList[idx:]:
                multap[multap.index(plugged)] = case
                isSwap = True
                break
            if latest < memo[plugged]:
                latest = memo[plugged]
        if not isSwap:
            multap[multap.index(memo.index(latest))] = case
    return counter

print(solution())


