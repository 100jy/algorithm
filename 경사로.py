# NxN 지도 높이가 적혀짐
# 가로 직선길 혹은 세로 직선 길 검토

# 경사로를 조건 따라 설치

# 지나갈 수 있는 길의 개수를 구하시오
# L길이의 받침 필요(다 닿아야함)
# 겹쳐놓기 불가능
# 높이 차이는 1까지

import sys
input = sys.stdin.readline


def get_input():
    N, L = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        line = map(int, input().split())
        for j, cont in enumerate(line):
            board[i][j] = int(cont)

    return N, L, board


def possible(line, idx, L, d, installed):
    if d:
        for i in range(1, L+1):
            if idx+i > N-1 or idx+i < 0:
                return False, 0
            if line[idx+i]+1 != line[idx] or\
                (installed[idx+i]):
                return False, 0
            installed[idx + i] = True
    else:
        for i in range(-1, -L-1, -1):
            if idx+i > N-1 or idx+i < 0:
                return False, 0

            if line[idx+i]+1 != line[idx] or\
                (installed[idx+i]):
                return False, 0
            installed[idx+i] = True

    return True, installed


def check(i, L, board, d):
    if d == 'h':
        line = board[i]
    else:
        line = [board[x][i] for x in range(N)]

    installed = [False] * N
    idx = 0

    while True:
        if idx == N-1:
            return True

        if line[idx] > line[idx+1]:
            chk, installed = \
                possible(line, idx, L, 1, installed)
            if chk:
                idx += L
            else:
                return False

        elif line[idx] < line[idx+1]:
            chk, installed = \
                possible(line, idx+1, L, 0, installed)
            if chk:
                idx += 1
            else:
                return False

        else:
            idx += 1


def main():
    global N
    N, L, board = get_input()

    cnt = 0

    for i in range(N):
        cnt += int(check(i, L, board, 'h'))
        cnt += int(check(i, L, board, 'v'))

    print(cnt)

    return


if __name__ == '__main__':
    main()
