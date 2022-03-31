from sys import stdin
input = stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

def solution():
  for i in range(1, n):
    for j in range(i+1):
      if j == 0:
        l[i][j] = l[i][j] + l[i-1][j]
      elif j == i:
        l[i][j] = l[i][j] + l[i-1][j-1]
      else:
        l[i][j] = l[i][j] + max(l[i-1][j-1], l[i-1][j])
    
  return max(l[n-1])

print(solution())