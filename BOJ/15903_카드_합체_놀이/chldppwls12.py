import heapq
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

def solution(n, m, cards):
  heapq.heapify(cards)
  for _ in range(m):
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    heapq.heappush(cards, c1+c2)
    heapq.heappush(cards, c1+c2)
  
  return sum(cards)

print(solution(n, m, cards))