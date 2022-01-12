import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    distance = list(map(int, input().split(' ')))
    city_cost = list(map(int, input().split(' ')))
    count = 1
    cost = distance[0] * city_cost[0]
    min_cost = city_cost[0]

    while count < N - 1:
        if (min_cost <= city_cost[count]):
            cost += min_cost * distance[count]
        else:
            cost += city_cost[count] * distance[count]
            min_cost = city_cost[count]
        count += 1
    return cost

print(solution())