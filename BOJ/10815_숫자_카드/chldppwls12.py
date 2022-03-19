from sys import stdin
input = stdin.readline

N = int(input())
sang_cards = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

def solution():
  ans = []
  set_sang_cards = set(sang_cards)
  for c in cards:
    if c in set_sang_cards:
      ans.append(1)
    else:
      ans.append(0)

  return ans

ans = solution()
print(' '.join(list(map(str, ans))))