# NxN 격자,
# 한마리 상어, M마리 물고기
# 아기상어 초기크기 2
# 한번에 좌우상하 한칸씩이동

# 자신보다 크기가 큰 물고기 있는 칸 못간다
# 자기보다 작은 물고기만 먹는다(같은 x)

# 먹을 수 있는 고기 없으면 종료
# 먹을 수 있는 물고기중 가장 가까운 거 먹음
# 동순위 열>행

# 자기와 크기와 같은 수 먹을떄마다 크기1증가

# 종료까지 총 먹은 횟수

import sys
from collections import defaultdict, deque
import heapq
input = sys.stdin.readline

def get_input():
    N = int(input())
    fishs = defaultdict(bool)
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)
            if int(cont) == 9:
                shark = (i,j)
            elif int(cont) != 0:
                fishs[(i,j)] = True

    return board, N, shark, fishs


def bfs(shark, goal, w):
    q = deque([(shark[0], shark[1], 0)])
    visit = [[False] * N for _ in range(N)]
    visit[shark[0]][shark[1]] = True

    while q:
        x, y, s = q.popleft()
        for dx, dy in [(1,0),(-1,0),
                       (0,-1), (0,1)]:
            new_x, new_y = x+dx, y+dy
            if 0<=new_x<N and 0<=new_y<N:
                if new_x == goal[0] and \
                        new_y == goal[1]:
                    return s+1, new_x, new_y

                if (board[new_x][new_y] <= w
                    or board[new_x][new_y] == 9)\
                    and not(visit[new_x][new_y]):
                    q.append((new_x, new_y, s+1))
                    visit[new_x][new_y] = True

    # d, x, y
    return float('inf'), -1, -1


def get_near(shark, fishs, w):
    arr_d = []
    for (x, y) in fishs.keys():
        # 물고기 있고 먹을 수 있다면
        if fishs[(x, y)] and board[x][y] < w:
            # 거리 측정
            heapq.heappush(arr_d, bfs(shark, (x, y), w))
    #잡을 물고기 없으면
    if not(arr_d):
        return float('inf'), shark, fishs

    # 물고기 먹고
    fishs[(arr_d[0][1], arr_d[0][2])] = False
    board[arr_d[0][1]][arr_d[0][2]] = 0
    # 좌표이동
    shark = (arr_d[0][1], arr_d[0][2])
    return arr_d[0][0], shark, fishs


def main():
    global board
    global N
    board, N, shark, fishs = get_input()
    s = 0
    w = 2
    cnt = 0
    while sum(fishs.values()) > 0:
        # 먹을 수 있는 최단거리 물고기 찾기
        d, shark, fishs = get_near(shark, fishs, w)

        # 없다면 종료
        if d == float('inf'):
            break
        # 있다면
        s += d
        # 먹은 횟수 늘리기
        cnt += 1
        # 횟수 무게와 같다면
        if cnt == w:
            w += 1
            cnt = 0

    #종료 후 시간간 print
    print(s)


if __name__ == '__main__':
    main()