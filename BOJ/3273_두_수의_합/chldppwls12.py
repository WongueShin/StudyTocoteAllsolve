from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
left = 0
right = n-1
ans = 0
while left < right:
  tmp = nums[left]+nums[right]
  if tmp == x:
    ans += 1
  if tmp < x:
    left += 1
    continue
  right -=1

print(ans)