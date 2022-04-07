from sys import stdin
input = stdin.readline

n = int(input())

def solution():
  memo = [[0]* 3 for _ in range(n+1)]
  memo[1][0] = 1
  memo[1][1] = 1
  memo[1][2] = 1
  
  for i in range(2, n+1):
    memo[i][0] = (memo[i-1][0] + memo[i-1][1] + memo[i-1][2]) % 9901
    memo[i][1] = (memo[i-1][0] + memo[i-1][2]) % 9901
    memo[i][2] = (memo[i-1][0] + memo[i-1][1]) % 9901

  return sum(memo[n]) % 9901

print(solution())