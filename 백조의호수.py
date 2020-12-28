#########BFS############################################
# 그래프와 시작점이 주어졌을때, 시작점에서 도달가능한 모든 간선을
# 탐색하여 찾는 과정
# 시작점으로 부터 거리를 하나씩 늘리며 정점을 발견한다.
# 직전 정점 그래프는 넓이우선탐색 트리가 된다.
########################################################
'''
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

from collections import deque
from collections import defaultdict

def BFS(G, s):
    # 초기화
    visit = defaultdict(int)
    Q = deque([])
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if visit[v] == 0:
                #v를 방문하고
                visit[v] = 1
                # v의 인접노드들을 넣어준다
                Q += G[v]
    return visit


print(BFS(graph, 'A'))
'''

#########문제풀이###############################################
# 백조, 물을 각각저장할 큐와 임시 큐를 2개씩 만들어 총 4개의 큐를 만듬
# 물에 대한 bfs로 얼음이 녹는 것을 구현
#
###############################################################
import sys
from collections import deque

def main():
    '''
    day : 경과일수
    visited : 방문처리 배열
    lake : 이차원 배열
    WaterQ : 접근가능 vertex 집합
    NextQ : 추가해야 할 vertex 집합
    swan : 탐색 시작위치
    goal : 목표점

    :return: days
    '''
    #입력처리
    R, C = sys.stdin.readline().split(' ')
    R = int(R)
    C = int(C)

    #초기화
    day = 0
    swan = None
    goal = None
    lake = []
    visited = []
    WaterQ = deque([])
    moves = [(1,0), (0,1), (-1,0), (0,-1)]

    # 하나씩 읽으면서 좌표에 저장
    for i in range(R):
        line = sys.stdin.readline()
        lake.append([0]*C)
        visited.append([False] * C)
        for j in range(C):
            cont = line[j]
            lake[i][j] = cont
            # 백조위치(시작점)와 goal 버택스들 저장
            if cont == 'L':
                if swan:
                    goal = (i, j)
                else:
                    swan = (i, j)
                WaterQ.append((i,j))
            elif cont == '.':
                WaterQ.append((i,j))

    # 탐색
    Q = deque([swan])
    visited[swan[0]][swan[1]] = True

    while True:
        while Q:
            v = Q.popleft()
            x, y = v[0], v[1]
            # TODO 초기화 까먹었었음..
            NextQ = deque([])

            for x_move, y_move in moves:
                x_new = x + x_move
                y_new = y + y_move

                # 두백조가 만났을시
                if (x_new, y_new) == goal:
                    print(day)
                    return None

                #경계 초과시, 방문했을시 제외
                if (x_new< 0) or (y_new< 0) or (x_new >= R) \
                        or (y_new >= C) or  visited[x_new][y_new] == True:
                    continue

                #탐색가능 영역
                elif lake[x_new][y_new] == '.':
                    Q.append((x_new, y_new))

                #NextQ 좌표저장(녹을 영역)
                elif (lake[x_new][y_new] == 'X'):
                    NextQ.append((x_new, y_new))

                visited[x_new][y_new] = True

        day += 1

        # 도달한 영역에서 시작
        Q = NextQ

        # waterQ에 녹여주기
        size = len(WaterQ)
        for i in range(size):
            x, y = WaterQ.popleft()

            for x_move, y_move in moves:
                x_new = x + x_move
                y_new = y + y_move

                if (x_new< 0) or (y_new< 0) or (x_new >= R) or (y_new >= C):
                        continue

                elif lake[x_new][y_new] == 'X':
                    lake[x_new][y_new] = '.'
                    WaterQ.append((x_new, y_new))


if __name__ == '__main__':
    main()





