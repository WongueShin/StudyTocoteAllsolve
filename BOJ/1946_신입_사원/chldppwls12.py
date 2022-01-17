from sys import stdin
input = stdin.readline

t = int(input())

def solution():
  n = int(input())
  l = []
  for _ in range(n):
    s1, s2 = map(int, input().split())
    l.append((s1, s2))

  l.sort()
  ml = l[0][1]
  ans = 1

  for i in range(1, n):
    if ml > l[i][1]:
      ans += 1
      ml = l[i][1]
  
  return ans

for _ in range(t):
  solution()