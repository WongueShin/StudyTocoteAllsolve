import sys
import heapq

def input():
    return sys.stdin.readline()

def compare(arr1, arr2):
    startT = arr1[0]
    endT = arr1[1]
    if arr2[0] <= startT:
        heapq.heappop(arr2)
        heapq.heappush(arr2, endT)
        return
    heapq.heappush(arr2, endT)
    return

def solution():
    N = int(input())
    classList = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
    classList.sort(key=lambda x: x[0])
    temp = [0]
    for ele in classList:
        compare(ele, temp)
    return len(temp)


print(solution())
"""
총 풀이시간: 35분

처음 아이디어.
    시작시간 기준으로 소팅후,
    총 필요한 강의실에 해당하는 리스트인 temp를 선언.
    temp의 ele는 그 강의실에서 진행되는 수업의 끝나는 시간을 의미하기 때문에,
    for로 순회하며, ele보다 startT가 작으면, temp[ele_idx] = endT가 된다.
    모두 종류후에, temp의 length를 반환하면 그게 정답이 된다.
    ===> 시간초과.
    heap을 사용해야하 제한시간 안에 풀이가 가능하다.
    이러한 풀이방법은 이미 알고있지만, 즉각적으로 떠올리지 못하네... 
    관련한 문제를 더 풀어보면서 감을 잡아보자!
"""