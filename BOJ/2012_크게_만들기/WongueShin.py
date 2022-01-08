import sys
def input():
    return sys.stdin.readline()

def solution():
    N, K = map(int, input().split(' '))
    num = list(map(int, input().rstrip()))
    counter = 0
    result = []

    for letter in num:
        if counter < K:
            if len(result) == 0:
                result.append(letter)
                continue
            if result[-1] < letter:
                while counter < K and result[-1] < letter:
                    counter += 1
                    result.pop()
                    if(len(result) == 0):
                        break
                result.append(letter)
                continue
        result.append(letter)
    if K > counter:
        result = result[:-K+counter]
    return ''.join(list(map(str,result)))
print(solution())
