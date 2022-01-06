import sys 

def input():
    return sys.stdin.readline()



def solution():
    N = int(input())
    Arr = list(map(int, input().split(' ')))
    Arr.sort()
    totalSum = 0
    for ele in Arr:
        if ele <= totalSum + 1:
            totalSum += ele
            continue
        break
    return totalSum + 1
print(solution())

"""
첫번째 드는 생각.
    n!의 시간복잡도로 sum(input arry)false가 넣어진 어레이를 선언하고,
    전체 케이스를 이중 for문으로 순회하며 계산한 결과를 Array[resulte] = true로 변경한 뒤에
    모두 계산이 완료된 후 순차조회후 제일 먼저 false가 나오는 인덱스가 답 or 하나도 없으면
    totalSum + 1이 답이된다.

근데... 들어오는 n의 개수가 1000...
1000!은 사실상 풀이가 불가능한 수.

그럼 분명히 다른 합리적인 알고리즘이 있을꺼라 생각이 든다.
sort후에 누적합을 더해가며 검사하는 알고리즘으로 풀이가 가능하다고 한다...
흠... 좀 지엽적인 문제라 생각이 드네. 풀이방법을 떠올리지 못한다고 해서 잘못된건 아닌거 같다.

풀이시간 = 20분 (첫번째 방법을 생각해보고 풀이 불가능하다 생각되서 바로 솔루션 검색)
"""