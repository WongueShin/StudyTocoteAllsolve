from sys import stdin
input = stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))

def solution(nums):
  if len(nums)%2 == 0:
    ans = nums[N//2 - 1]
  else:
    ans = nums[N//2]

  return ans

print(solution(nums))