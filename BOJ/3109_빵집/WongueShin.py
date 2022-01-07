import sys
def input():
    return sys.stdin.readline()
count = 0
def solve(i,j):
    global count
    count+=1
    if j == C-1:
        return True
    for d in dx:
        if 0<=i+d<R and grid[i+d][j+1]=="." and not visit[i+d][j+1]:
            visit[i+d][j+1] = True
            if solve(i+d, j+1):
                return True
    return False

R, C = map(int, input().rstrip("\n").split())
grid = []
visit = [[False]*C for _ in range(0,R)]
for i in range(0,R):
    grid.append(list(input().rstrip("\n")))
dx = [-1,0,1]
ans = 0
for i in range(0,R):
    if grid[i][0] == ".":
        if solve(i,0):
            ans+=1

print(ans)