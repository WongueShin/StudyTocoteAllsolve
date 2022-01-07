import heapq
from sys import stdin
input = stdin.readline

def solution():
  n = int(input())
  t_list = [list(map(int, input().split())) for _ in range(n)]

  t_list.sort()
  classroom = []
  heapq.heappush(classroom, t_list[0][1])

  for i in range(1, len(t_list)):
    if t_list[i][0] < classroom[0]:
      heapq.heappush(classroom, t_list[i][1])
    else:
      heapq.heappop(classroom)
      heapq.heappush(classroom, t_list[i][1])
  
  return len(classroom)

print(solution())