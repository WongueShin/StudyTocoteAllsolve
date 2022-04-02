from sys import stdin

def input():
    return stdin.readline().rstrip()

def solution():
    N = int(input())

    cost_list = []
    for _ in range(N):
        cost_list.append(tuple(map(int, input().split())))

    result_list = [cost_list[0]]

    for i in range(1, N):
        r_result = min(result_list[i - 1][1], result_list[i - 1][2]) + cost_list[i][0]
        g_result = min(result_list[i - 1][0], result_list[i - 1][2]) + cost_list[i][1]
        b_result = min(result_list[i - 1][0], result_list[i - 1][1]) + cost_list[i][2]
        result_list.append([r_result, g_result, b_result])

    print(min(result_list[N - 1]))

solution()