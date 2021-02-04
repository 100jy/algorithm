#########################################
# BFS 풀이
#########################################


def solution(board):
    from collections import deque
    global answer
    answer = 0
    global cost_arr
    cost_arr = []

    def BFS(q, board=board):

        visit = [[float('inf')] * len(board) for x in range(len(board))]
        visit[0][0] = 0

        def get_new(x, y, d, new_d, cost):
            if d == 0:
                new_cost = cost+100
            elif new_d != d:
                new_cost = cost+600
            else:
                new_cost = cost+100

            if new_d == 'R':
                new_x, new_y = x, y+1
            elif new_d == 'L':
                new_x, new_y = x, y-1
            elif new_d == 'U':
                new_x, new_y = x-1, y
            else:
                new_x, new_y = x+1, y

            return new_x, new_y, new_cost

        while q:
            #빼내서 4방향으로 검토하고 큐에 넣기
            x, y, d, cost = q.popleft()
            for new_d in ['U','D','L','R']:
                new_x, new_y, new_cost = get_new(x,y,d,new_d,cost)
                # 도착시 저장
                if new_x == len(board)-1 and new_y == len(board)-1:
                    global cost_arr
                    cost_arr.append(new_cost)
                    continue
                # 범위 넘을시 탐색x
                if not((0<=new_x<len(board)) and (0<=new_y<len(board))):
                    continue
                # 장애물 있을시 탐색x
                # 최저비용 경로가 아니면 탐색x
                if board[new_x][new_y] != 1:
                    if new_cost <= visit[new_x][new_y]:
                        q.append([new_x, new_y, new_d, new_cost])
                        visit[new_x][new_y] = new_cost


    BFS(deque([[0,0,0,0]]))
    answer = min(cost_arr)
    return answer


###################################
# BFS 최단경로 구하기 빠름
# 장애물있는 최단 경로
###################################
