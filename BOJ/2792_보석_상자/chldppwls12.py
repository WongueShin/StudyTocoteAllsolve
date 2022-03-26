from sys import  stdin
input = stdin.readline

N, M = map(int,input().split())
jl = [int(input()) for _ in range(M)]

def solution():
  left = 1
  right = max(jl)

  while left <= right:
    mid = (left+right)//2
    cnt = 0
    for j in jl:
      if j%mid == 0:
        cnt += j//mid
      else:
        cnt += j//mid + 1

    if cnt > N:
      left = mid+1
    else:
      right = mid-1

  return left

print(solution())