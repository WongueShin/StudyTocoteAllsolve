from collections import deque
from sys import stdin
input = stdin.readline

def solution():
  tops = [deque(list(map(int, input().rstrip()))) for _ in range(4)]

  k = int(input())
  rotates = deque(list(map(int, input().split())) for _ in range(k))

  while rotates:
    tidx, r = rotates.popleft()
    tidx -= 1
    tmp2 = tops[tidx][2]
    tmp6 = tops[tidx][6]
    tmpr = r
    tops[tidx].rotate(r)

    #시작 톱니 왼쪽 방향
    for i in range(tidx-1, -1, -1):
      if tops[i][2] != tmp6:
        tmp6 = tops[i][6]
        tops[i].rotate(r*-1)
        r *= -1
      else:
        break
    
    r = tmpr
    #시작 톱니 오른쪽 방향
    for i in range(tidx+1, 4):
      if tops[i][6] != tmp2:
        tmp2 = tops[i][2]
        tops[i].rotate(r*-1)
        r *= -1
      else:
        break
  
  ans = 0
  for i in range(4):
    if tops[i][0] == 1:
      ans += 2**i
  return ans

print(solution())