from sys import stdin
input = stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

def solution():
  for i in range(1, n):
    l[i][0] = min(l[i-1][1], l[i-1][2]) + l[i][0]
    l[i][1] = min(l[i-1][0], l[i-1][2]) + l[i][1]
    l[i][2] = min(l[i-1][0], l[i-1][1]) + l[i][2]
  
  return min(l[n-1][0], l[n-1][1], l[n-1][2])

print(solution())