from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    X, Y = map(int, input().split(' '))
    Z = (Y * 100) // X
    if Z >= 99:
        print(-1)
        return
    
    ans = 0
    left = 1
    rigth = X

    while True:
        if left > rigth:
            print(ans)
            return 
        mid = (left + rigth) // 2
        if (Y+mid)*100 // (X+mid) <= Z:
            left = mid + 1
            continue
        ans = mid
        rigth = mid - 1

solution()
