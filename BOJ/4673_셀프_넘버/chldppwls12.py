def check(n):
  sum = n
  while True:
    if n == 0:
      break
    sum += n%10
    n = n//10

  return sum

def solution():
  self_list = [True] * 10001
  for i in range(1, 10001):
    num = check(i)

    if num < 10001:
      self_list[num] = False

  for i in range(1, 10001):
    if self_list[i]:
      print(i)

solution()