import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    R, C, N = map(int, input().split(' '))
    mat = [list(input()) for _ in range(R)]
    
    for j in range(R):
        for i in range(C):
            if mat[j][i] == 'O':
                mat[j][i] = 2
    rangeList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for time in range(1, N):
        for j in range(R):
            for i in range(C):
                if mat[j][i] == '.':
                    mat[j][i] = time + 3
        for j in range(R):
            for i in range(C):
                if mat[j][i] == '.':
                    continue
                if mat[j][i] == time:
                    mat[j][i] = '.'
                    for case in rangeList:
                        dj = j + case[0]
                        di = i + case[1]
                        if not(0 <= dj and dj < R and 0 <= di < C):
                            continue
                        if mat[dj][di] == time:
                            continue
                        mat[dj][di] = '.' 
    ans = []
    for line in mat:
        temp = ''
        for letter in line:
            if letter == '.':
                temp += '.'
                continue
            temp += 'O'
        ans.append(temp)
    for i in ans:
        print(i)

solution()