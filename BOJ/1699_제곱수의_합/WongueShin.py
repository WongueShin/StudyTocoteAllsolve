from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    n = int(input())
    memo = [i for i in range (n+1)]
    for i in range(1,n+1):
        for j in range(1,i):
            if j*j > i :
                break
            if memo[i] > memo[i-j*j] + 1 :
                memo[i] = memo[i-j*j] + 1
    print(memo[n])

solution()