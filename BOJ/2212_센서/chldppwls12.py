from sys import stdin
input = stdin.readline

n = int(input())
k = int(input())
num_list = list(map(int, input().split()))

def solution(n, k, num_list):
  ans = 0
  if (k >= n):
    return ans
  else:
    num_list.sort()
    diff_list = []
    for i in range(len(num_list)-1):
      diff_list.append(num_list[i+1]-num_list[i])
    
    diff_list.sort()
    ans = sum(diff_list[:n-k])

    return ans

print(solution(n, k, num_list))