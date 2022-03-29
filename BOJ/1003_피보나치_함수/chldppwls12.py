from sys import stdin
input = stdin.readline

t = int(input())

def solution():
  n = int(input())
  zero = [1, 0, 1]
  one = [0, 1, 1]

  if n >= 3:
    for i in range(3, n+1):
      zero.append(zero[i-1]+zero[i-2])
      one.append(one[i-1]+one[i-2])

  print('{} {}' .format(zero[n], one[n]))

for _ in range(t):
  solution()