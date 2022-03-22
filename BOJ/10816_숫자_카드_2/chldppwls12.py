from sys import stdin
input = stdin.readline

N = int(input())
sang_cards = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

d = {}

def solution():
  for i in sang_cards:
    d[i] = d.get(i, 0) + 1

  ans = []
  for i in cards:
    ans.append(d.get(i, 0))

  return ans

ans = solution()
print(' '.join(list(map(str, ans))))