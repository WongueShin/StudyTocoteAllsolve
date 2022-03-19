from sys import stdin
input = stdin.readline

t = int(input())

def solution():
  n = int(input())
  nums = [input().rstrip() for _ in range(n)]
  nums.sort()

  for i in range(n-1):
    if nums[i] == nums[i+1][:len(nums[i])]:
      return 'NO'
  return 'YES'

for _ in range(t):
  print(solution())