from sys import stdin
input = stdin.readline

N = int(input())
l = [int(input().rstrip()) for _ in range(N)]

def solution(l):
  l.sort(reverse=True)

  for i in range(len(l)-2):
    if l[i] < l[i+1] + l[i+2]:
      ans = l[i] + l[i+1] + l[i+2]
      return ans
  
  return -1

print(solution(l))