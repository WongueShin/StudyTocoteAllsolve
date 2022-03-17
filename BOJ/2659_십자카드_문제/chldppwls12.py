from collections import deque
from sys import stdin
from collections import deque
input = stdin.readline

nums = deque(map(int, input().split()))

def getcl(nums):
  cl = 10000
  for _ in range(4):
    now = nums[0]*1000 + nums[1]*100 + nums[2]*10 + nums[3]*1
    if now < cl:
      cl = now
    nums.rotate(1)
  return cl

cl = getcl(nums)

ans = 0
for i in range(1111, cl+1):
  ideq = deque(map(int, str(i)))
  if getcl(ideq) == i:
    ans += 1

print(ans)