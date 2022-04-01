from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())
    memo = [1,1,1,2,2]
    for i in range(5, N):
        memo.append(memo[i - 1] + memo[i - 5])
    print(memo[N - 1])
    
T = int(input())
for _ in range(T):
    solution()