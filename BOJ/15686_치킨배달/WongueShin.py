import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def solution():
    def computeCase(cases):
        result = 0
        for house in houseList:
            temp = []
            for case in cases:
                temp.append(abs(house[0] - case[0]) + abs(house[1] - case[1]))
            result += min(temp)
        return result

    N, M = map(int, input().split(' '))
    mat = [list(map(int, input().split(' '))) for _ in range(N)]
    houseList = []
    chickenList = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                houseList.append((j + 1, i + 1))
                continue
            if mat[i][j] == 2:
                chickenList.append((j + 1, i + 1))
    # print(houseList, chickenList)
    caseList = list(combinations(chickenList, M))
    mincase = computeCase(caseList[0])
    for case in caseList:
        mincase = min(mincase, computeCase(case))
    return mincase

print(solution())