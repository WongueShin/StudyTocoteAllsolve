from sys import stdin
input = stdin.readline

n = int(input())
ll = list(map(int, input().split()))

def solution():
  left = 0
  right = len(ll)-1
  ans = [abs(ll[left]+ll[right]), (ll[left],ll[right])]
  
  while left <= right:
    tot = ll[left]+ll[right]
    if abs(tot) < ans[0]:
        ans[0] = abs(tot)
        ans[1] = (ll[left],ll[right])
    if tot > 0:
        right-=1
    elif tot < 0:
        left += 1
    else:
        return ans[1]
  return ans[1]

ans = solution()
print("{} {}".format(ans[0], ans[1]))
