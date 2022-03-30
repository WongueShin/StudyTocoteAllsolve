import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    memo = {1 : 1, 2: 3}
    print(DnQ(n, memo)% 10007)

def DnQ(n, memo):
    if n in memo:
        return memo[n]
    #case 01 1x2 => Dnq(n - 1)
    #case 02 2x1 => Dnq(n -2)
    temp = DnQ(n - 1, memo) + 2*DnQ(n-2, memo)
    memo[n] = temp
    return temp

sys.setrecursionlimit(10000*10)
solution()