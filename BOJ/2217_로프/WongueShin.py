import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    ropeList = [int(input()) for _ in range(N)]
    ropeList.sort(reverse= True)
    ans = ropeList[0]
    for idx in range(N):
        ans = max(ans, ropeList[idx] * (idx+ 1))
    return ans

print(solution())