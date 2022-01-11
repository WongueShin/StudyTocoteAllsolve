from sys import stdin
input = stdin.readline

n = int(input())
word_list = [input().rstrip() for _ in range(n)]

def check(word):
  alpha = [False]*26
  alpha[ord(word[0])-97] = True
  for i in range(1, len(word)):
    #이전 단어와 동일하지 않다면
    if word[i-1] != word[i]:
      if alpha[ord(word[i])-97]:
        return False
      alpha[ord(word[i])-97] = True
    #이전 단어와 동일하다면
    else:
      continue
  return True

def solution(n, word_list):
  cnt = 0
  for word in word_list:
    if check(word):
      cnt += 1

  return cnt

print(solution(n, word_list))