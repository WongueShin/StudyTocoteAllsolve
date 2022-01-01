from sys import stdin
input = stdin.readline

n = int(input())
time = list(map(int, input().split()))

def func(time):
  ans = 0
  time.sort()
  for i in range(n):
    ans += time[i] * (n-i)
  return ans

print(func(time))