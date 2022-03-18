from collections import deque
from sys import stdin
input = stdin.readline

word = deque(input().rstrip())

def solution(word):
  words = [''.join(word)]
  while len(word) > 1:
    word.popleft()
    words.append(''.join(word))

  words.sort()
  return words

ans = solution(word)

for a in ans:
  print(a)