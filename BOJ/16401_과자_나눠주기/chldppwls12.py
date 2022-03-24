from sys import stdin
input = stdin.readline

M, N = map(int, input().split())
nl = list(map(int, input().split()))

def solution():
  ans = 0
  left = 1
  right = max(nl)

  while left <= right:
    mid = (left+right)//2
    if sum([n//mid for n in nl]) >= M:
      ans = mid
      left = mid+1
    else:
      right = mid-1

  return ans

print(solution())