from sys import stdin
input = stdin.readline

N, C = map(int, input().split())
hl = [int(input()) for _ in range(N)]

def solution():
  hl.sort()

  left = 1
  right = hl[-1] - hl[0]

  while left <= right:
    mid = (left+right)//2
    cur = hl[0]
    cnt = 1

    for i in range(1, N):
      if hl[i] >= cur+mid:
        cnt += 1
        cur = hl[i]

    if cnt >= C:
      left = mid+1
      ans = mid
    else:
      right = mid-1

  return ans

print(solution())