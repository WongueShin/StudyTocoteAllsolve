from sys import stdin
input = stdin.readline

def solution():
  n, k = map(int, input().split())
  p_list = list(map(int, input().split()))
  cur_list = []
  ans = 0

  for i in range(k):
    if p_list[i] in cur_list:
      continue
    if len(cur_list) < n:
      cur_list.append(p_list[i])
      continue
    
    idx_list = []

    for j in range(n):
      try:
        idx = p_list[i:].index(cur_list[j])
      except:
        #다음 사용 순서가 없을 경우
        idx = 101
      idx_list.append(idx)

    p_out = idx_list.index(max(idx_list)) #다음 사용 순서가 없거나 가장 멀리있는 경우
    del cur_list[p_out]
    cur_list.append(p_list[i])
    ans += 1

  return ans

print(solution())