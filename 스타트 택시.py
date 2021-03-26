# 제한사항 있는 문제

# 손님 도착마다 연료 충전
# 연료 바닥나면 끝

# NxN 격자
# 최단경로로만 이동
# M명의 승객 M번에 이동

# 탟to승 최단거리 -> 행짧 > 열짧
# 연료 1칸당 1씩 소모
# 승객 내려주면 2배 충전

# 연료 바닥나면 실패


# 출력
# 남은 연료량(실패시 -1)

from collections import deque
import sys
import heapq


def get_input():
    inp = sys.stdin.readline
    N, M, oil = map(int, inp().split())
    board = [[0] * N for _ in range(N)]

    for i in range(N):
        line = map(int, inp().split())
        for j, cont in enumerate(line):
            board[i][j] = cont

    t_x, t_y = map(int, inp().split())
    p = [0] * M
    dest = [0] * M

    for i in range(M):
        x, y, x_to, y_to = map(int, inp().split())
        p[i] = (x-1, y-1)
        dest[i] = (x_to-1, y_to-1)
        # 승객있을 시 -1
        board[x-1][y-1] = -1

    return N, M, oil, board, t_x-1, t_y-1, p, dest


def get_passenger(t_x, t_y, oil):
    global p
    if (t_x,t_y) in p:
        idx = p.index((t_x, t_y))
        return 0,idx

    global board
    q = deque([(t_x, t_y, 0, oil)])
    global N
    visit = [[False] * N for _ in range(N)]
    visit[t_x][t_y] = True
    candidate = []
    s_min = float('inf')
    while q:
        a, b, s, o = q.popleft()

        #기름 다쓰면 조기에 중단
        if o < 0:
            return float('inf'), 0

        if s > s_min:
            break

        for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            new_x, new_y = a+dx, b+dy

            if 0<=new_x<N and 0<=new_y<N:
                global board
                # 승객 있는 좌표일 시
                if (new_x,new_y) in p:
                    idx = p.index((new_x, new_y))
                    heapq.heappush(candidate, (s+1, new_x, new_y, idx))

                    if s+1 < s_min:
                        s_min = s+1

                # 벽이 아니고 방문하지 않았다면
                if board[new_x][new_y] != 1 and \
                        not(visit[new_x][new_y]):
                    q.append((new_x, new_y, s+1, o-1))
                    visit[new_x][new_y] = True

    if candidate:
        # 같은 거리중 최소 거리와 인덱스
        return candidate[0][0], candidate[0][-1]

    # 목표 승객 거리와 인덱스
    return float('inf'), 0


def get_shortest(t_x, t_y, x, y, oil):

    if (t_x, t_y) == (x, y):
        return 0

    # BFS
    q = deque([(t_x, t_y, 0, oil)])
    global N
    visit = [[False] * N for _ in range(N)]
    visit[t_x][t_y] = True

    while q:
        a, b, s, o = q.popleft()

        #기름 다쓰면 조기에 중단
        if o < 0:
            return float('inf')

        for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            new_x, new_y = a+dx, b+dy

            if 0<=new_x<N and 0<=new_y<N:

                if (new_x, new_y) == (x, y):
                    return s+1

                global board
                if board[new_x][new_y] != 1 and \
                        not(visit[new_x][new_y]):
                    q.append((new_x, new_y, s+1, o-1))
                    visit[new_x][new_y] = True

    return float('inf')



def main():

    global board
    global N
    global p

    N, M, oil, board, t_x, t_y, p, dest = \
        get_input()
    cnt = M

    # 손님 남아있는 동안
    while cnt:
        # 가장 가까운 손님 찾고
        # M번 돌지 말고 제일 먼저 찾는 좌표 뽑기
        s, idx = get_passenger(t_x, t_y, oil)

        # 손님까지 가고
        x_s, y_s = p.pop(idx)
        t_x, t_y = x_s, y_s
        oil -= s

        if oil <= 0:
            break

        # 손님 태우고 이동
        x_to, y_to = dest.pop(idx)
        spend_oil = get_shortest(t_x, t_y, x_to, y_to, oil=oil)
        t_x, t_y = x_to, y_to
        oil -= spend_oil

        # 손님줄이고
        cnt -= 1

        if oil <= 0:
            # 완료면 기름 충전
            if not(cnt) and oil == 0:
                oil += 2*spend_oil
            break

        else:
            oil += 2*spend_oil


    # 손님 남아있다면
    if cnt>0:
        print(-1)
    elif oil>0:
        print(oil)
    else:
        print(-1)

if __name__ == '__main__':
    main()