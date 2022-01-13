from collections import deque
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

def solution(n, k):
  dq = deque(i+1 for i in range(n))
  ans = []
  while dq:
    dq.rotate(-k+1)
    ans.append(dq.popleft())
  
  return '<' + ', '.join(map(str, ans)) + '>'

print(solution(n, k))