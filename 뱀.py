# NxN 격자, 사과가 놓임
# 0,0 에서 시작, 길이는 1
# 처음에 오른쪽을 향함

#매초마다이동
# 머리를 늘려 다음칸에 위치
# 사과있다면 사과없어지고 꼬리 x(길이 한칸 증가)
# 없다면 몸길이 줄이고 꼬리칸을 움직여서 비움(길이유지)

#게임이 끝나는 시간 예측

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def get_input():
    N = int(input())
    K = int(input())
    apple = defaultdict(bool)
    query = defaultdict(bool)

    for i in range(K):
        x, y = map(int, input().split())
        apple[(x-1, y-1)] = True

    L = int(input())

    for i in range(L):
        # t초가 끝난 뒤 d방향으로 회전
        t, d = input().split()
        query[int(t)] = d

    return N, K, apple, query


def move(snake, apple, query, t):

    #이동
    d = snake['d']
    mapper = {'L' : (0,-1),'R' : (0,1),
              'U' : (-1,0), 'D' : (1,0)}

    dx, dy = mapper[d]

    new_head = (snake['body'][0][0] + dx,
                        snake['body'][0][1] + dy)

    # 종료 조건 확인
    if new_head[0] < 0 or new_head[0]>(N-1) or \
        new_head[1] < 0 or new_head[1] > (N - 1):
        return 0, 0, True

    if board[new_head[0]][new_head[1]]:
        return 0, 0, True

    # 사과있으면
    if apple[(new_head[0], new_head[1])]:
        snake['body'].appendleft(new_head)
        board[new_head[0]][new_head[1]] = True
        apple[(new_head[0], new_head[1])] = False

    # 없으면
    else:
        snake['body'].appendleft(new_head)
        board[new_head[0]][new_head[1]] = True
        # 꼬리비우기
        tail_x, tail_y = snake['body'].pop()
        board[tail_x][tail_y] = False

    # 방향전환
    if query[t] == 'L':
        m = {'D': 'R', 'L': 'D', 'U': 'L', 'R': 'U'}
        snake['d'] = m[d]
    if query[t] == 'D':
        m = {'R' : 'D', 'D':'L','L':'U','U':'R'}
        snake['d'] = m[d]

    return apple, snake, False


def main():
    global N, K, board
    N, K, apple, query = \
        get_input()
    board = [[False] * N for _ in range(N)]
    board[0][0] = True

    t = 0
    snake = { 'd':'R', 'body' : deque([(0,0)])}

    while True:
        t += 1
        # 벽 또는 자기자신과 부딛히면 끝
        apple, snake, death = move(snake, apple, query, t)

        if death:
            print(t)
            break


if __name__ == '__main__':
    main()