from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int ,input().split())
num_list = list(map(int, input().rstrip()))

def solution(n, k, num_list):
  dq = deque()
  for num in num_list:
    while len(dq)!=0 and dq[-1]<num and k>0:
      k-=1
      dq.pop()
    dq.append(num)

  ans = []
  while len(dq) > k:
    ans.append(dq.popleft())

  return ''.join(list(map(str, ans)))

print(solution(n, k, num_list))