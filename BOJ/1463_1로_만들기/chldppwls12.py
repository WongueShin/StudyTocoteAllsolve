from sys import stdin
input = stdin.readline

n = int(input())

def solution():
  ml = [0] *(n+1)

  for i in range(2, n+1):
    ml[i] = ml[i-1]+1

    if i%2 == 0:
      ml[i] = min(ml[i], ml[i//2]+1)
    if i%3 == 0:
      ml[i] = min(ml[i], ml[i//3]+1)
  
  return ml[n]

print(solution())