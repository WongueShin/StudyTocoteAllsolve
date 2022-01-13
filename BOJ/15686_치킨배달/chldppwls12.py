from sys import stdin
from itertools import combinations
input = stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

def dist(c1, c2):
  x1, y1 = c1
  x2, y2 = c2
  return abs(x1-x2) + abs(y1-y2)

def solution(n, m, g):
  houses = []
  chickens = []

  for i in range(n):
    for j, val in enumerate(g[i]):
      if val == 1:
        houses.append((i,j))
      elif val == 2:
        chickens.append((i,j))

  ans = 987654321
  for com in combinations(chickens, m):
    tot = 0
    for house in houses:
      tot += min(dist(house, chicken) for chicken in com)

    ans = min(ans, tot)

  return ans

print(solution(n, m, g))
