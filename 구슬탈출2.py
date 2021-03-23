# 빨간구슬 나오는 최소
# 좌우 상하
# bfs
# 빨간 구슬만 빠져나오고 파란은 나오면 안됨

#보드입력
# input 처리
N, M = map(int, input().split())
#board
board = [[0] * M for _ in range(N)]
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

# DFS
global min_cost
min_cost = M*N + 1

def dfs(r, b, cost, d):
    # 파란 구슬이 나가면 중단
    if b == goal:
        return
    # 10번을 넘으면 중단
    if cost > 10:
        return
    # 빨간공이 구멍이면 중단
    if r == goal:
        # 최솟값인지 점검
        global min_cost
        if cost < min_cost:
            min_cost = cost
        return

    # 4방향 탐색
    for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:

        #직전에 왔던 길 되돌아가면 중단
        if (d[0]+x) == 0 and (d[1]+y) == 0:
            return

        while True:
            new_r = (r[0] + x, r[1] + y)
            new_b = (b[0] + x, b[1] + y)
            # 파란공이 벽만나면 안움직임
            if board[new_b[0]][new_b[1]]=='#':
                # 이떄 빨간공이 파란공을 만나면 중단
                if new_r == b:
                    new_r = r
                    new_b = b
                    break
                else:
                    new_b = b

            if board[new_r[0]][new_r[1]]=='#':
                # 둘다 움직이지 않으면 탐색 중단
                if board[new_b[0]][new_b[1]]=='#':
                    return

            # 빨간공이 벽이나
            if board[new_r[0]][new_r[1]]=='#':
                new_r = r
                # 빨간공이 벽이고 파란공이 빨간공 만나도 안움직임
                if new_b == r:
                    new_b = b
                break
            # 구멍 만나면 중단
            if new_r == goal:
                break

            #좌표갱신
            r, b = new_r, new_b

        d = (x, y)
        # 공이 멈추면 기회를 한번 더하고 다음 탐색
        dfs(new_r, new_b, cost+1, d)


if __name__ == '__main__':
    dfs(init_r, init_b, 0, (0,0))

    # 갱신이 되지 않았다면 -1
    if min_cost == M*N + 1:
        min_cost = -1

    print(min_cost)


