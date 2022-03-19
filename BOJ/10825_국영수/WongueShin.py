import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    studentList = [(lambda x:(x[0], int(x[1]), int(x[2]), int(x[3])))(input().split(' '))  for _ in range(N)]
    studentList.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))
    for i in range(N):
        print(studentList[i][0])
    
solution()