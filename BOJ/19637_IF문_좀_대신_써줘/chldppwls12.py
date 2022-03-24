from sys import stdin
from bisect import bisect_left
input = stdin.readline

N, M = map(int, input().split())

l = []
dic = {}
for i in range(N):
  x, y= input().split()
  l.append(int(y))
  dic[i] = x

for _ in range(M):
  print(dic[bisect_left(l, int(input()))])

# dic = {}
# for _ in range(N):
#   w, lr = input().split()
#   dic[w] = int(lr)

# def solution(level):
#   for w, l in dic.items():
#     if level <= l:
#       return w

# for _ in range(M):
#   print(solution(int(input())))