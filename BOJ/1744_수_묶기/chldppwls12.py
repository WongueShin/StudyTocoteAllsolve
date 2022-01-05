from sys import stdin
input = stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]

def solution(num_list):
  ans = 0
  positive_list = []
  negative_list = []

  for num in num_list:
    if num > 1:
      positive_list.append(num)
    elif num <= 0:
      negative_list.append(num)
    elif num == 1:
      ans += 1
  
  positive_list.sort(reverse=True)
  negative_list.sort()

  if len(positive_list) % 2 == 0:
    for i in range(0, len(positive_list), 2):
      ans += positive_list[i] * positive_list[i+1]
  else:
    for i in range(0, len(positive_list)-1, 2):
      ans += positive_list[i] * positive_list[i+1]
    ans += positive_list[-1]

  if len(negative_list) % 2 == 0:
    for i in range(0, len(negative_list), 2):
      ans += negative_list[i] * negative_list[i+1]
  else:
    for i in range(0, len(negative_list)-1, 2):
      ans += negative_list[i] * negative_list[i+1]
    ans += negative_list[-1]
  
  return ans

print(solution(num_list))