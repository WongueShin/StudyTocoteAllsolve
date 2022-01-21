from sys import setrecursionlimit, stdin
setrecursionlimit(10**8)
def input():
    return stdin.readline().rstrip()

def solution():
    N=int(input())
    graph = {i:{} for i in range(N)}
    totalLink = 0
    for i in range(N):
        inputList = list(map(int, input().split()))
        for j in range(N):
            if inputList[j] > 0:
                totalLink += j
            graph[i][j] =  inputList[j]
    if totalLink%2 == 1:
        return -1

    def dfs(now):
        print(now + 1, end=' ')
        for next in graph[now]:
            if graph[now][next]> 0:
                graph[now][next] -= 1
                graph[next][now] -= 1
                
                dfs(next)
        return 

    dfs(0)

solution()
