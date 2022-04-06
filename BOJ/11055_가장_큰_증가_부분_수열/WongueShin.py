from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    n=int(input())
    array=list(map(int, input().split()))

    memo=[1]*n
    memo[0]=array[0]
    for i in range(1,n):
        for j in range(i):
            if array[j]<array[i]:
                memo[i]=max(memo[i], memo[j]+array[i])
                continue
            memo[i]=max(memo[i], array[i])

    print(max(memo))

solution()