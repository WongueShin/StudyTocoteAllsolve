from sys import  stdin
input = stdin.readline

N, M = map(int, input().split())
gl = list(map(int ,input().split()))

def solution():
  left = max(gl)
  right = sum(gl)
  ans = 987654321

  while left <= right:
    cnt = 0
    mid = (left+right)//2
    suml = 0

    for i in range(N):
      if suml+gl[i] > mid:
        cnt += 1
        suml = 0
      suml += gl[i]

    if suml:
      cnt += 1

    if cnt <= M:
      ans = min(ans, mid)
      right = mid-1
    else:
      left = mid+1

  return ans

print(solution())