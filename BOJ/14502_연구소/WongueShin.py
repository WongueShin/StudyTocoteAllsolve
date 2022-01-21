import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
graph_copy = copy.deepcopy(graph) 
dx, dy = [-1,1,0,0], [0,0,-1,1] 

safe_region = 0 

def dfs(x,y,sel_wall):
    sel_wall[x][y] = 2 

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if sel_wall[nx][ny] == 0:
                dfs(nx,ny,sel_wall) 



def select_wall(start, count):
    global safe_region

    if count == 3: 
        sel_wall = copy.deepcopy(graph_copy) 
        for i in range(N):
            for j in range(M):
                if sel_wall[i][j] == 2: 
                    dfs(i,j,sel_wall)
        safe_count = sum(_.count(0) for _ in sel_wall) 
        safe_region = max(safe_region,safe_count) 
        return

    else: 
        for i in range(start, N*M): 
            r = i // M 
            c = i % M 
            if graph_copy[r][c] == 0: 
                graph_copy[r][c] = 1 
                select_wall(i,count+1) 
                graph_copy[r][c] = 0 

select_wall(0,0)
print(safe_region)