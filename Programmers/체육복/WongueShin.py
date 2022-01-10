
testCase = [[5, [2, 4], [1, 3, 5]], [5, [2, 4], [3]], [3, [3], [1]],[1,[1],[1]]]

def solution(input):
    n, lost, reserve = input
    temp = [1 for _ in range(n)]
    for case in lost:
        temp[case - 1] -=1
    for case in reserve:
        temp[case - 1] +=1
    if n == 1:
        return temp[0]
    if n == 2:
        result = sum(temp)
        if result > 3:
            return result
        return 2
    
    for idx in range(n-2):
        # [2, 0, ]
        if temp[idx] == 2 and temp[idx + 1] == 0:
            temp[idx] = 1
            temp[idx + 1] =1
            continue
        # [0, 2, ]
        if temp[idx] == 0 and temp[idx + 1] == 2:
            temp[idx]= 1
            temp[idx+1] =1
            continue
        # [ , 0, 2]
        if temp[idx + 1] == 0 and temp[idx + 2] == 2:
            temp[idx +1 ] =1
            temp[idx + 2] = 1
    counter = 0
    for ele in temp:
        if ele > 0:
            counter += 1
    return counter

for case in testCase:
    print(solution(case))