#  A= 65 Z= 90

def solution(name):
    print(name)
    temp = [letter for letter in name]
    print(temp)
    asciied = list(map(ord, temp))
    print(asciied)
    goal = []
    for letter in asciied:
        goal.append(min(letter - 65, 91 - letter))
    print(goal)
    current = [65 for _ in range(len(temp))]
    cursor = 0
    counter = 0
    que = []
    for idx in range(len(temp)):
        if current[idx] != asciied[idx]:
            que.append(idx)
    print(que)
    while len(que) > 0:
        print(f'current: {list(map(chr, current))}')
        if current[cursor] != asciied[cursor]:
            counter += goal[cursor]
            current[cursor] = asciied[cursor]
            que.pop(que.index(cursor))
            continue
        nextIdx = cursor
        for ele in range(que):
            nextIdx = ele
            if que[ele] > cursor:
                break
        next = min(que[nextIdx] - cursor, que[nextIdx - 1])
        
    return counter


testCase = ["JEROEN", "JAN"]
for case in testCase:
    print(solution(case))

    9 + 15