import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    inputList = [int(input()) for _ in range(N)]
    inputList.sort()
    print(int(round(sum(inputList)/N)))
    print(inputList[N//2])
    dict = {}
    for ele in inputList:
        if ele not in dict:
            dict[ele] = 1
            continue
        dict[ele] += 1
    Memo = [(dict[i], i) for i in dict]
    Memo.sort(reverse=True)
    i = 0
    ModeList = []
    
    while i < len(Memo) and Memo[i][0] == Memo[0][0]:
        ModeList.append(Memo[i][1]) 
        i += 1
    ModeList.sort()
    if len(ModeList) == 1:
        print(ModeList[0])
    else:
        print(ModeList[1])
    if len(inputList) == 0:
        print(0)
    else:
        print(inputList[-1] - inputList[0])

solution()