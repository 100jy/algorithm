# NxM
# cctv 다섯 종류
# 방향  전체 감시
# 벽은 통과 못함
# 감시 못하는 지역은 사각지대

# cctv 90도 회전가능
# 0은 빈칸 6은 벽 1~5는 cctv

# CCTV 방향 조절해서
# 사각지대의 최솟값 구하기
# 사각지대 = 전체 0 중 감시 가능 뺸부분

import sys
from collections import defaultdict
input = sys.stdin.readline


def get_input():
    N, M = map(int, input().split())
    space = defaultdict(bool)
    cctv = []
    board = [[0] * M for _ in range(N)]

    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)
            if cont == '0':
                space[(i, j)] = False
            if 0 < int(cont) < 6:
                cctv.append((i, j, int(cont)))

    return N, M, board, space, cctv


def get_black(space):
    # 해당 영역에서 False 세줌
    cnt = 0
    for light in space.values():
        if not(light):
            cnt += 1
    return cnt


def watch(x, y, type, space, board, d):

    def go(x, y, d, space):
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        a, b = x, y
        while True:
            a = a + dir[d][0]
            b = b + dir[d][1]
            if 0 <= a < N and 0 <= b < M and \
                    board[a][b] != 6:
                if board[a][b] == 0:
                    space[(a, b)] = True
            else:
                break
        return space

    # 빛 밣히면 True로
    if type == 1:
        space = go(x, y, d, space)

    elif type == 2:
        mapper = [2, 3, 0, 1]
        space = go(x, y, d, space)
        space = go(x, y, mapper[d], space)

    elif type == 3:
        space = go(x, y, d, space)
        space = go(x, y, (d+1) % 4, space)

    elif type == 4:
        mapper = [2, 3, 0, 1]
        space = go(x, y, d, space)
        space = go(x, y,  mapper[d], space)
        space = go(x, y, (d + 1) % 4, space)

    elif type == 5:
        space = go(x, y, 0, space)
        space = go(x, y, 1, space)
        space = go(x, y, 2, space)
        space = go(x, y, 3, space)

    return space


def get_min(board, space, cctv, d):
    #DFS
    if d == len(cctv):
        global min_black
        num = get_black(space)
        if num < min_black:
            min_black = num
        return

    for i in range(4):
        (x, y, type) = cctv[d]
        # 5번유형은 한번만 계산
        if type == 5:
            if i > 0:
                continue
        tmp_space = space.copy()
        new_space = watch(x, y, type, tmp_space, board, i)
        get_min(board, new_space, cctv, d+1)


def main():
    global N
    global M

    N, M, board, space, cctv\
        = get_input()
    # cctv들 방향 조합하고
    # 사각지대 계산하기
    global min_black
    min_black = float('inf')
    get_min(board, space, cctv, 0)
    print(min_black)


if __name__ == '__main__':
    main()

