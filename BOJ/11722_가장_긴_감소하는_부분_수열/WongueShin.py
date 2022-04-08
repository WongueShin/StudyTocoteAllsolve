from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    memo = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[j] > nums[i]:
                memo[i] = max(memo[i],memo[j]+1)
    print(max(memo))

solution()