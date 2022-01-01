from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coin_type = [int(input().rstrip())for _ in range(n)]

def func(money):
  ans = 0
  for coin in coin_type[::-1]:
    if (money == 0):
      break
    ans += money // coin
    money %= coin

  return ans

print(func(k))