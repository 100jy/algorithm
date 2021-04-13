# NxM 지도
# 주사위 처음애는 다0



#주사위 이동떄마다 상단에 쓰인 값 출력

# 지도 바깥명령은 무시하고 출력x

import sys
input = sys.stdin.readline


def get_input():
    N, M, x, y, K =\
        map(int, input().split())

    board = [[0] * M for _ in range(N)]

    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)

    query = list(map(int, input().split()))

    return N, M, x, y, K, board, query


def roll(dice, x, y, q):
    c_dice = dice.copy()
    d = [(0,1),(0,-1),(-1,0),(1,0)]
    new_x, new_y = x + d[q - 1][0], y + d[q - 1][1]
    if new_x < 0 or new_x > (N - 1) or \
            new_y < 0 or new_y > (M - 1):
        return dice, x, y, False
    if q == 1:
        dice['r'] = c_dice['d']
        dice['l'] = c_dice['u']
        dice['u'] = c_dice['r']
        dice['d'] = c_dice['l']
        dice['f'] = c_dice['f']
        dice['b'] = c_dice['b']
    if q == 2:
        dice['r'] = c_dice['u']
        dice['l'] = c_dice['d']
        dice['u'] = c_dice['l']
        dice['d'] = c_dice['r']
        dice['f'] = c_dice['f']
        dice['b'] = c_dice['b']
    if q == 3:
        dice['r'] = c_dice['r']
        dice['l'] = c_dice['l']
        dice['u'] = c_dice['f']
        dice['d'] = c_dice['b']
        dice['f'] = c_dice['d']
        dice['b'] = c_dice['u']
    if q == 4:
        dice['r'] = c_dice['r']
        dice['l'] = c_dice['l']
        dice['u'] = c_dice['b']
        dice['d'] = c_dice['f']
        dice['f'] = c_dice['u']
        dice['b'] = c_dice['d']

    # 이동칸에 0이면 주사위 바닥면이 칸에복사
    if board[new_x][new_y] == 0:
        board[new_x][new_y] = dice['d']

    # 0이아니면 바닥면 숫자가 칸에복사
    # 칸에 쓰인수는 0이 됨
    else:
        dice['d'] = board[new_x][new_y]
        board[new_x][new_y] = 0

    return dice, new_x, new_y, True



def main():
    global N, M, board
    N, M, x, y, K, board, query =\
        get_input()
    dice = {'u':0,'d':0,'l':0,'r':0, 'f':0, 'b':0}
    # K번 명령 시행하면서 주사위 굴리고
    for i in range(K):
        dice, x, y, ch = roll(dice, x, y,query[i])
        # 윗면의 수 출력
        if ch:
            print(dice['u'])


if __name__ == '__main__':
    main()