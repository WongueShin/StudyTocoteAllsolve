from sys import stdin

def input():
    return stdin.readline().rstrip()

def dp(last, current):
    global st_score_list, memo

    if (last, current) in memo:
        return memo[(last, current)]

    if current == len(st_score_list) - 1:
        return 0

    if last == current == -1:

        if len(st_score_list) >= 2:
            val = max(st_score_list[0] + dp(-1, 0), st_score_list[1] + dp(-1, 1))
            memo[(last, current)] = val
            return val
        memo[(last, current)] = st_score_list[0]
        return st_score_list[0]

    if last == -1 and current >= 0:
        if current + 2 <= len(st_score_list) - 1:
            val = max(st_score_list[current + 1] + dp(current, current + 1),
                      st_score_list[current + 2] + dp(current, current + 2))
            memo[(last, current)] = val
            return val
        val = st_score_list[current + 1] + dp(current, current + 1)
        memo[(last, current)] = val
        return val

    if current - last == 1:
        if current + 2 <= len(st_score_list) - 1:
            val = st_score_list[current + 2] + dp(current, current + 2)
            memo[(last, current)] = val
            return val
        return -10e10

    if current + 2 <= len(st_score_list) - 1:
        val = max(st_score_list[current + 1] + dp(current, current + 1),
                  st_score_list[current + 2] + dp(current, current + 2))
        memo[(last, current)] = val
        return val
    val = st_score_list[current + 1] + dp(current, current + 1)
    memo[(last, current)] = val
    return val


def sol():
    global st_score_list, memo
    N = int(input())  # number of stairs
    st_score_list = [int(input()) for _ in range(N)]
    memo = {}
    print(dp(-1, -1))


sol()