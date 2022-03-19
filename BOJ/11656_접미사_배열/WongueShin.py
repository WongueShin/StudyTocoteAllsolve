import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    inputStr = input()
    sliceList = sorted([inputStr[i:] for i in range(len(inputStr))])
    for ele in sliceList:
        print(ele)

solution()