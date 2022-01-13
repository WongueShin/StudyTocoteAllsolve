import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    N, L = map(int, input().split(' '))
    l = list(map(int, input().split(' ')))
    l.sort()
    ans = 0
    last = l[0]
    for case in l:
        if case - last < L:
            continue
        ans += 1
        last = case
    return ans + 1

print(solution())