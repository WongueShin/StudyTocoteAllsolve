from collections import Counter
from sys import stdin
input = stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

def solution(N, nums):
  nums.sort()
  print(round(sum(nums)/N))
  print(nums[N//2])
  cnt = Counter(nums).most_common(2)
  if len(cnt) > 1:
    print(cnt[1][0]) if cnt[0][1] == cnt[1][1] else print(cnt[0][0])
  else:
    print(cnt[0][0])
  print(max(nums)-min(nums))

solution(N, nums)