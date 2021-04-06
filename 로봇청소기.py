# 청소하는 영역의 개수
# NxM 장소, 벽 혹은 빈칸
# 청소기는 방향이 있음
# 동서남북중 하나

# 로봇이 청소하는 칸의 개수를 구하라

import sys
input = sys.stdin.readline

def get_input():
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    for i in range(N):
        line = input().split()
        for j,cont in enumerate(line):
            board[i][j] = int(cont)

    return N, M, r, c, d, board


def check(r, c, next_d, board):
    # 왼쪽 방향에 청소 안한곳 존재하는가?
    d = [(-1, 0),(0,1),(1,0),(0,-1)]

    new_r = r + d[next_d][0]
    new_c = c + d[next_d][1]
    if 0>new_r or new_r>N-1 or \
            0 > new_c or new_c > M - 1:
        return False
    if board[new_r][new_c]==0:
        return True


def main():
    global N, M
    N, M, r, c, d, board = \
        get_input()

    # 청소기 작동
    cnt = 0
    ro = 0

    while True:
        # 북동남서
        mapper = {0 : (3, (0, -1), (1,0)), 3: (2, (1, 0),(0,1)),
                  1 : (0, (-1, 0), (0,-1)), 2: (1, (0, 1),(-1,0))}

        # 방향 전환후
        next_d, (dr, dc), (bx, by) = mapper[d]
        new_r, new_c = r+dr, c+dc

        chk = check(r, c, next_d, board)

        # 현재칸이 먼지있다면
        if board[r][c] == 0:
            # 청소하고
            board[r][c] = 2
            # 칸수 추가
            cnt += 1

        # 이동없이 한반퀴 다돌면
        if ro==4:
            ro = 0
            # 방향 유지하고 후진
            r, c = r + bx, c + by
            # 뒤가 벽이면 중단
            if board[r][c] == 1:
                print(cnt)
                return
            continue

        #앞칸이 벽이면
        if board[new_r][new_c] == 1:
            ro += 1
            #다른 방향 검토
            d = next_d
            continue

        #앞칸이 청소면
        if chk:
            d = next_d
            r, c = new_r, new_c
            ro = 0
            continue

        # 청소할곳없다면
        # 회전만
        else:
            d = next_d
            ro += 1
            continue


if __name__ == '__main__':
    main()




