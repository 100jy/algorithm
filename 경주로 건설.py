def solution(board):
    import sys
    sys.setrecursionlimit(10000)
    global answer
    answer = 1e+10

    def DFS(x, y, d, cost, visit, board=board):
        # 범위 벗어나는 경우 return
        global answer
        if (0>x) or (len(board)-1 <x) or 0>y or len(board)-1 <y:
            return
        if cost>answer:
            return
        # 도착한 경우 점수 갱신
        if (x == len(board)-1) and (y == len(board)-1):
            if cost < answer:
                answer = cost
            return
        else:
            # 앞으로
            if (x<len(board)-1):
                if board[x+1][y] != 1 and d != 'L':
                    # 안꺽는 경우
                    if d == 'R' or d == 0:
                        new_cost = cost+100
                    # 꺽는 경우
                    else:
                        new_cost = cost+600
                    visit[x+1][y] = 1
                    DFS(x+1, y, 'R', new_cost, visit)

            # 아래로
            if (y<len(board)-1):
                if board[x][y+1] != 1 and d != 'U':
                    # 안꺽는 경우
                    if d == 'D' or d == 0:
                        new_cost = cost+100
                    # 꺽는 경우
                    else:
                        new_cost = cost+600
                    visit[x][y+1] = 1
                    DFS(x, y+1, 'D', new_cost, visit)

            # 위로
            if (0<y):
                if board[x][y-1] != 1 and d != 'D':
                    # 안꺽는 경우
                    if d == 'U' or d == 0:
                        new_cost = cost+100
                    # 꺽는 경우
                    else:
                        new_cost = cost+600
                    visit[x][y-1] = 1
                    DFS(x, y-1, 'U', new_cost, visit)

            # 뒤로
            if (0<x):
                if board[x-1][y] != 1 and d != 'R':
                    # 안꺽는 경우
                    if d == 'L' or d == 0:
                        new_cost = cost+100
                    # 꺽는 경우
                    else:
                        new_cost = cost+600
                    visit[x-1][y] = 1
                    DFS(x-1, y, 'L', new_cost, visit)

    visit = [[0] * len(board) for x in range(len(board))]
    DFS(0,0,0,0,visit)
    return answer

###################################
#시간 초과 Queue 이용한 방법 써보기...
###################################