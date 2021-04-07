# NxM
# 0 빈칸 1 벽 2 바이러스
# 벽 3개 다세우거
# 바이러스는 벽없으면
# 상하좌우로 퍼짐

# 안전영역의 최댓값
# 벽 세개 세우고 (빈칸 중 3개 뽑기)
# (빈칸 - 바이러스가 퍼진 영역)

import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque


def get_input():
    N, M = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    virus = []
    blank = []
    num_blank = 0
    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)
            if cont == '2':
                virus.append((i, j))

            elif cont == '0':
                blank.append((i, j))
                num_blank += 1

    return N, M, board, virus, blank, num_blank


def BFS(virus, num_blank):
    # 벽 3개 세움
    cnt = num_blank - 3
    q = deque(virus)
    visit = [[False] * M for _ in range(N)]
    for i, j in q:
        visit[i][j] = True

    while q:
        a, b = q.popleft()
        for dx, dy in [(1, 0),(-1,0),(0,1),(0,-1)]:
            new_a, new_b = a+dx, b+dy
            if 0<=new_a<N and 0<=new_b<M:
                    if board[new_a][new_b] == 0 and\
                        not(visit[new_a][new_b]):
                        q.append((new_a, new_b))
                        visit[new_a][new_b] = True
                        cnt -= 1

    return cnt


def main():
    global N, M, board
    N, M, board, virus, blank, num_blank = \
        get_input()
    max_cnt = -float('inf')
    # 벽 3개 고르고
    combs = combinations(blank, 3)

    for walls in combs:
        # 해당 벽 세운 뒤
        for w in walls:
            board[w[0]][w[1]] = 1
        # BFS하고
        cnt = BFS(virus, num_blank)
        # 개수 구하고 최댓값 갱신
        if cnt > max_cnt:
            max_cnt = cnt
        # 보드 원래대로
        for w in walls:
            board[w[0]][w[1]] = 0

    print(max_cnt)

    return


if __name__ == '__main__':
    main()


