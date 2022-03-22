from sys import stdin
input = stdin.readline

K, N = map(int, input().split())
ll = [int(input()) for _ in range(K)]

def solution():
  left = 1
  right = max(ll)
  ans = 0

  while left <= right:
    mid = (left+right)//2
    cnt = sum([l//mid for l in ll])

    if cnt >= N:
      ans = mid
      left = mid+1
    else:
      right = mid-1

  return ans

print(solution())