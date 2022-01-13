import sys
def input(): 
    return sys.stdin.readline().rstrip()

def solution():
    def move(direction):
        if direction == 1:
            dice[0],dice[2],dice[5],dice[3] = dice[3],dice[0],dice[2],dice[5]
        elif direction == 2:
            dice[3],dice[0],dice[2],dice[5] = dice[0],dice[2],dice[5],dice[3]
        elif direction == 3:
            dice[1],dice[5],dice[4],dice[0] = dice[0],dice[1],dice[5],dice[4]
        elif direction == 4:
            dice[0],dice[1],dice[5],dice[4] = dice[1],dice[5],dice[4],dice[0]

    n,m,x,y,k = map(int,input().split())
    dice = [0 for _ in range(6)] 
    board = [list(map(int,input().split())) for _ in range(n)]
    board_move = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

    for order in map(int,input().split()):
        dx,dy = board_move[order]
        dx+=x; dy+=y
        if n>dx>=0 and m>dy>=0:
            move(order)
            if not board[dx][dy]:
                board[dx][dy] = dice[5]
            else:
                board[dx][dy],dice[5] = 0,board[dx][dy]
            print(dice[0])
            x,y = dx,dy

solution()