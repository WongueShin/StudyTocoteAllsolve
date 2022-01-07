from sys import stdin
input = stdin.readline

l = input().rstrip()

def func(l):
  ans_arr = []
  arr = l.split('-')
  for i in arr:
    a = i.split('+')
    ans_arr.append(sum(list(map(int, a))))

  return ans_arr[0] - sum(ans_arr[1:])

print(func(l))