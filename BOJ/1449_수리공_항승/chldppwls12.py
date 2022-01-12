from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
w_list = list(map(int, input().split()))

def solution(n, l, w_list):
  w_list.sort()
  cur = 0
  ans = 0
  for w in w_list:
    if cur < w:
      cur = w+l-1
      ans += 1
  return ans

print(solution(n, l, w_list))