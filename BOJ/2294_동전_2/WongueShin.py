from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    n, k = map(int, input().split())

    li =[]

    for i in range(n):
        li.append(int(input()))

    memo = [10001] * (k+1)
    memo[0] = 0

    for num in li:
        for i in range(num, k+1):
            memo[i] = min(memo[i],memo[i-num]+1)
    if memo[k] == 10001:
        print(-1)
        return
    print(memo[k])

solution()