from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

N = int(input())
sang_cards = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

def solution():
  sang_cards.sort()
  ans = []

  for c in cards:
    ans.append(bisect_right(sang_cards, c) - bisect_left(sang_cards, c))

  return ' '.join(list(map(str, ans)))

print(solution())