# RxC 격자판
# 칸은 미세먼지의 양

# 미세먼지 확산

# 공기 청정기 작동


# T초후 남아있는 미세먼지의 양

import sys
input = sys.stdin.readline

def get_input():
    R, C, T = map(int, input().split())

    class machine:
        def __init__(self):
            self.up = None
            self.down = None

    m = machine()
    dust_sum = 0
    board = [[0] * C for _ in range(R)]
    for i in range(R):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)
            # 최초먼지
            if int(cont) > 0:
                dust_sum += int(cont)

            # 청정기 좌표 기록
            if int(cont) == -1:
                if m.up:
                    m.down = (i, j)
                else:
                    m.up = (i,j)

    return R, C, T, board, m, dust_sum


def spread(board, m):
    new_board = [[0] * C for _ in range(R)]
    new_board[m.up[0]][m.up[1]] = -1
    new_board[m.down[0]][m.down[1]] = -1
    # 모든칸에서
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                next_axis = []
                # 인접한 네방향으로 이동
                for dx, dy in [(1,0), (-1,0),
                               (0,1), (0,-1)]:
                    new_x, new_y = i + dx, j + dy
                    # 범위내고 공기청정기 없을 시에만
                    if 0<=new_x<R and 0<=new_y<C:
                        if board[new_x][new_y] != -1:
                            next_axis.append((new_x, new_y))

                amt = board[i][j] // 5
                if next_axis:
                    for x, y in next_axis:
                        #각칸에 1/5씩
                        new_board[x][y] += amt
                        # 남은 양은 퍼뜨리고 남은양
                    new_board[i][j] += board[i][j] - \
                                amt * len(next_axis)
                else:
                    new_board[i][j] += board[i][j]

    return new_board


def blow(board, m):
    new_board = []
    for i in range(R):
        tmp = [x for x in board[i]]
        new_board.append(tmp)

    removed = 0
    # 바람 순환하고
    # 미세먼지가 바람의 방향으로 1칸씩 이동
    # 윗순환
    # R
    r, c = m.up
    new_board[r][1] = 0
    new_board[r][2:] = board[r][1:-1]

    # U
    for x in range(r, 0, -1):
        new_board[x-1][-1] = board[x][-1]
    # L
    new_board[0][:-1] = board[0][1:]
    # D
    for x in range(0, r-1):
        new_board[x+1][0] = board[x][0]
    # 공기청정기로 오면 사라짐
    removed += board[r-1][c]

    # 아랫순환
    # R
    r, c = m.down
    new_board[r][1] = 0
    new_board[r][2:] = board[r][1:-1]

    # D
    for x in range(r, R-1):
        new_board[x+1][-1] = board[x][-1]

    # L
    new_board[-1][:-1] = board[-1][1:]

    # U
    for x in range(R-1, r+1, -1):
        new_board[x-1][0] = board[x][0]

    # 공기청정기로 오면 사라짐
    removed += board[r+1][c]

    return new_board, removed


def main():
    global R
    global C

    R, C, T, board, m, dust_sum = get_input()

    for i in range(T):
        # 미세먼지 확산
        board = spread(board, m)
        # 공기 청정기 작동
        board, removed = blow(board, m)
        dust_sum -= removed

    print(dust_sum)

    return None


if __name__ == '__main__':
    main()
