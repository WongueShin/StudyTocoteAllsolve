import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    cardList = list(map(int, input().split(' ')))
    memo = {}
    for ele in cardList:
        memo[ele] = True
    M = int(input())
    testcase = list(map(int, input().split(' ')))
    returnStr = ''
    for case in testcase:
        if case in memo:
            returnStr += '1 '
            continue
        returnStr += '0 '
    print(returnStr.rstrip())

solution()

