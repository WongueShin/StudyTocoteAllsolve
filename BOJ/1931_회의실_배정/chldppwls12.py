from sys import stdin
input = stdin.readline

def solution():
  n = int(input())
  t_list = [list(map(int, input().split())) for _ in range(n)]

  ans = 1
  t_list.sort(key = lambda x: (x[1], x[0]))

  finish = t_list[0][1]
  for i in range(1, n):
    if finish <= t_list[i][0]:
      ans += 1
      finish = t_list[i][1]
  
  return ans

print(solution())