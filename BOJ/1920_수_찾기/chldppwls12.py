from sys import stdin
input = stdin.readline

n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))

def binary_search(left, right, value):
  if left > right:
    return -1
  
  mid = (left+right)//2

  if nl[mid] > value:
    return binary_search(left, mid-1, value)
  elif nl[mid] < value:
    return binary_search(mid+1, right, value)
  else:
    return mid

def solution():
  nl.sort()

  left = 0
  right = n-1

  for value in ml:
    ans = binary_search(left, right, value)
    if ans == -1:
      print(0)
    else:
      print(1)

solution()