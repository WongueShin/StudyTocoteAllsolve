from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

def solution(n, k):
  cnt = 0
  nums = [True] * (n+1)
  for i in range(2, n+1):
    for j in range(i, n+1, i):
      if nums[j] == True:
        nums[j] = False
        cnt += 1
        if cnt == k:
          return j

print(solution(n, k))