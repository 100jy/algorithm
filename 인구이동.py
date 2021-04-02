# NxN, 각칸이 나라
# A는 인구수
# 인구이동 없을 떄까지 지속

# 인구이동 발생 건수

import sys
from collections import deque
input = sys.stdin.readline

def get_input():
    N, L, R = map(int, input().split())
    A = [[0] * N for _ in range(N)]

    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            A[i][j] = int(cont)

    return N, L, R, A


def bfs(x, y, visit, A):
    q = deque([(x, y)])
    visit[x][y] = True
    path = [(x, y)]
    sum_pop = A[x][y]

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0),
                       (0,1), (0, -1)]:
            new_x, new_y = x+dx, y+dy

            if 0<=new_x<N and 0<=new_y<N:
                const = abs(A[new_x][new_y] - A[x][y])

                if not(visit[new_x][new_y]) and\
                        L<=const<=R:
                    q.append((new_x, new_y))
                    path.append((new_x, new_y))
                    sum_pop += A[new_x][new_y]
                    visit[new_x][new_y] = True

    return sum_pop, len(path), path, visit


def move(A):
    #BFS
    # 모든 시작 위치에서
    visit = [[False] * N for _ in range(N)]
    new_A = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not(visit[x][y]):
                sum_pop, s, path, visit = bfs(x, y, visit, A)
                for a, b in path:
                    new_A[a][b] = sum_pop // s
    # 영역 만들어지면
    # 인구 분배
    return new_A




def main():
    global N
    global L
    global R
    N, L, R, A = get_input()
    cnt = 0
    while True:
        new_A = move(A)
        if new_A == A:
            print(cnt)
            return None
        else:
            A = new_A
            cnt += 1

if __name__ == '__main__':
    main()
