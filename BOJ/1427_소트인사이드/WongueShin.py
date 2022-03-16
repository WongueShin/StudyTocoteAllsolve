import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    inputValue = [int(i) for i in str(input())]
    inputValue.sort(reverse=True)
    
    print(''.join(map(str,inputValue)))

solution()