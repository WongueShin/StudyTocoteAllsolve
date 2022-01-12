import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    A = list(map(int,input().split(' ')))
    B = list(map(int,input().split(' ')))
    A.sort()
    B.sort(reverse=True)
    return sum([A[i]*B[i] for i in range(N)])

print(solution())