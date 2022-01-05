from sys import stdin
input = stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

def func(a_list, b_list, n):
  ans = 0
  for i in range(n):
    ans += a_list[i] * b_list[i]
  
  return ans

print(func(a_list, b_list, n))