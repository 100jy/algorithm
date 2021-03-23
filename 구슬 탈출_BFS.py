#보드입력
# input 처리
N, M = map(int, input().split())
#board
board = [[0] * M for _ in range(N)]
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# 라인 단위로 받아서 분배
for i in range(N):
    line = input()
    for j, cont in enumerate(line):
        if cont == 'O':
            #구멍의 위치
            goal = (i, j)
        if cont == 'R':
            # 초기 빨간공 좌표
            init_r = (i, j)
        if cont == 'B':
            # 초기 파란공 좌표
            init_b = (i, j)
        board[i][j] = cont

visit[init_r[0]][init_r[1]][init_b[0]][init_b[1]] = True

# BFS
from collections import  deque
n = 1
# [((z, b),(c,d))]
q = deque([((init_r, init_b),n)])

def move(axis, i, board=board):
    case = [(0,1),(0,-1),(1,0),(-1,0)]
    new_axis = []

    # 빨간공도 파란공도 끝까지 가야함
    cnt_arr = []
    for x, y in axis:
        cnt = 1
        while True:
            new_x = x + case[i][0]
            new_y = y + case[i][1]

            if board[new_x][new_y] == '#':
                new_axis.append((x,y))
                break
            elif (new_x, new_y) == goal:
                new_axis.append((new_x,new_y))
                break
            else:
                x = new_x
                y = new_y
            cnt+=1
        cnt_arr.append(cnt)

    # 이동 결과 겹치면
    if new_axis[0] == new_axis[1] and (new_axis[0] != goal):
        # 더적게 움직인 쪽 한칸 전으로 이동
        if cnt_arr[0] > cnt_arr[1]:
            new_axis[0] = new_axis[0][0] - case[i][0], new_axis[0][1] - case[i][1]
        else:
            new_axis[1] = new_axis[1][0] - case[i][0], new_axis[1][1] - case[i][1]

    return new_axis


def bfs():
    while q:
        # 좌표가져오기
        axis, n = q.popleft()
        if n > 10:
            break
        # 4방으로 이동
        for i in range(4):
            new_axis = move(axis, i)
            # 빨간공이 골에 도착한 경우
            if (new_axis[0] == goal) and (new_axis[1] != goal):
                print(n)
                return
            # 탐색중지 조건들
            # 파란공이 들어간 경우
            cond1 = (new_axis[1] == goal)
            # 빨간공이 왔던 길을 또간 경우
            cond2 = visit[new_axis[0][0]][new_axis[0][1]][new_axis[1][0]][new_axis[1][1]]
            if not(cond1) and not(cond2):
                # 나온좌표들, 현재 횟수 추가
                q.append(((new_axis), n+1))
                visit[new_axis[0][0]][new_axis[0][1]][new_axis[1][0]][new_axis[1][1]] = True
    # 가능한 경우 없을 경우
    print(-1)


if __name__ == '__main__':
    bfs()


######### 개선점 #####################
# ~(AUB) = A^c inter B^c : 드모르간 법칙
# 장애물, 이동 : bfs 풀이
# 좌표 2개 -> 방문 처리에 4차원 배열
#####################################
