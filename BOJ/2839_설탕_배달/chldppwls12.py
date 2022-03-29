from sys import stdin
input = stdin.readline

n = int(input())

def solution():
  m = [987654321] * (n+5)
  m[3] = m[5] = 1

  for i in range(6, n+1):
    m[i] = min(m[i-3], m[i-5]) + 1
  
  if m[n] < 987654321:
    return m[n]
  else:
    return -1

print(solution())