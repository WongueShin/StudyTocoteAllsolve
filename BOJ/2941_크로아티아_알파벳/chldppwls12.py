from sys import stdin
input = stdin.readline

word = input().rstrip()

def solution(word):
  alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
  for alpha in alpha_list:
    if alpha in word:
      word = word.replace(alpha, '.')

  return len(word)

print(solution(word))