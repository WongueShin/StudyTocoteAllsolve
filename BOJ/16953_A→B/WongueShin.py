import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    A, B = map(int, input().split(' '))
    counter = 0
    while True:
        if B == A:
            return counter + 1
        
        if B < A:
            return -1

        if B%10 == 1:
            B //= 10
            counter += 1
            continue
        
        if B%2 != 0:
            return -1

        if B%10 != 1:
            B //= 2
            counter += 1
            
print(solution())