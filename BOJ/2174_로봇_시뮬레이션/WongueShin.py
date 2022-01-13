import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    A, B = map(int, input().split(' '))
    N, M = map(int, input().split(' '))
    location = []
    commandList = []
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for _ in range(N):
        temp = input().split(' ')
        if temp[2] == 'N':
            temp[2] = 0
        if temp[2] == 'E':
            temp[2] = 1
        if temp[2] == 'S':
            temp[2] = 2
        if temp[2] == 'W':
            temp[2] = 3
        location.append([int(temp[0]), int(temp[1]), temp[2]])
    for _ in range(M):
        temp = input().split(' ')
        commandList.append((int(temp[0]), temp[1], int(temp[2])))

    mat = [[-1 for i in range(A)] for j in range(B)]
    for idx in range(N):
        robot = location[idx]
        mat[-robot[1]][robot[0] - 1] = idx

    for command in commandList:
        #print(f'command: {command}')
        robotNum = command[0] - 1
        robotPositon = location[robotNum][:2]
        robotDirection = location[robotNum][2]
        #print(f'robotNum: {robotNum} positon: {robotPositon}  direction: {robotDirection}')
        if command[1] == 'L':
            robotDirection = robotDirection - command[2]
            if robotDirection < 0:
                robotDirection = -(abs(robotDirection)%4)
            location[robotNum][2] = robotDirection
            continue

        if command[1] == 'R':
            robotDirection = (robotDirection + command[2])%4
            location[robotNum][2]= robotDirection
            continue

        if command[1] == 'F':
            for i in range(command[2]):
                robotPositon[0] += direction[robotDirection][0]
                robotPositon[1] += direction[robotDirection][1]
                #print(robotPositon)
                if A < robotPositon[0] or robotPositon[0] < 1 or B < robotPositon[1]or robotPositon[1] < 0:
                    #print(f'robot positon : {robotPositon}')
                    return f'Robot {robotNum + 1} crashes into the wall'
                if mat[-robotPositon[1]][robotPositon[0]- 1] != -1:
                    return f'Robot {robotNum + 1} crashes into robot {mat[-robotPositon[1]][robotPositon[0] - 1] + 1}'
                
            location[robotNum][0] = robotPositon[0]
            location[robotNum][1] = robotPositon[1]
            mat[-location[robotNum][1]][location[robotNum][0] - 1] = robotNum


    return 'OK'

print(solution())