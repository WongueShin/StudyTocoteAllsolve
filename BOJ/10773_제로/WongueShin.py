import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    z = []
    for i in range(n):
        num = int(input())
        if num == 0:
            z.pop()
        else:
            z.append(num)
    return(sum(z))

print(solution())