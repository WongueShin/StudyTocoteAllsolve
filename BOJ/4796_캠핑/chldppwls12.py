from sys import stdin
input = stdin.readline

def solution():
  tc = 1
  while True:
    l, p, v = map(int, input().split())
    if l == 0:
      break
    print(f'Case {tc}: {v//p*l + min(v%p, l)}')
    tc+=1

solution()