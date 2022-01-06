from sys import stdin
input = stdin.readline

def solution():
  n = int(input())
  w_list = list(map(int, input().split()))

  w_list.sort()

  if w_list[0] != 1:
    return 1
  
  total = w_list[0]

  for i in range(1, n):
    if w_list[i] > total + 1:
      break
    total += w_list[i]
  
  return total + 1

print(solution())