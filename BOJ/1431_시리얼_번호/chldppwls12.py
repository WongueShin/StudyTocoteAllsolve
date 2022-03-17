from sys import stdin
input = stdin.readline

N = int(input())
nums = [input().rstrip() for _ in range(N)]

def solution(N, nums):
  ans = []
  for num in nums:
    cnt = 0
    for s in num:
      if s.isdigit():
        cnt+=int(s)
    ans.append((num, cnt))

  ans.sort(key=lambda x: (len(x[0]), x[1], x[0]))
  for a in ans:
    print(a[0])

solution(N, nums)