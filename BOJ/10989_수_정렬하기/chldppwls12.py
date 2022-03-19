from sys import stdin
input = stdin.readline

N = int(input())

def solution():
  l = [0]*10001
  for _ in range(N):
    l[int(input())] += 1
  
  for i in range(1, 10001):
    if l[i] != 0:
      for _ in range(l[i]):
        print(i)

solution()