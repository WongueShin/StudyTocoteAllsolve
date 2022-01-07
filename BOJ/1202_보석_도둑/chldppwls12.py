import heapq
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
j_list = []
for _ in range(n):
  heapq.heappush(j_list, list(map(int, input().split())))
w_list = [int(input()) for _ in range(k)]

def solution(j_list, w_list):
  ans = 0
  w_list.sort()

  p_list = []
  for w in w_list:
    while j_list and w >= j_list[0][0]:
      [w, v] = heapq.heappop(j_list)
      heapq.heappush(p_list, (-v, v))

    if p_list:
      ans += heapq.heappop(p_list)[1]
    elif not j_list:
      break
  
  return ans

print(solution(j_list, w_list))