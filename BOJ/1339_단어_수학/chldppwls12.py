from sys import stdin
input = stdin.readline

n = int(input())
word_list = [input().rstrip() for _ in range(n)]

def func(word_list):
  word_dict = {}

  for word in word_list:
    for i, w in enumerate(word):
      if w in word_dict.keys():
        word_dict[w] += 10 ** (len(word) - (i+1))
      else:
        word_dict[w] = 10 ** (len(word) - (i+1))

  sort_list = sorted(word_dict.values(), reverse=True)

  num = 9
  ans = 0

  for i in sort_list:
    ans += i * num
    num -= 1

  return ans

print(func(word_list))