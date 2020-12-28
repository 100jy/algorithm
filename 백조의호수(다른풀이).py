#####################풀이#######################################
# 1. 백조, 물을 각각 저장할 큐와 임시 큐를 2개씩 총4개생성
# 2. 얼음이 녹는 것을 물이 이동하는 것(4방으로)처리 -> 물에 대한 BFS
# 3. 다음칸이 빙판이면 바로녹이지 않고 임시큐에 넣는다.
# 4. 백조가 이동가능한 곳까지 이동(다음칸이 빙판이면 임시큐에 넣는다.)
# 5. 백조가 만나지 못하면 물과 백조를 각각 임시큐로 치환하고 임시큐 초기화
# 6. 만날때까지 반복
################################################################

from collections import deque
import sys


input  = sys.stdin.readline

#상하좌우 이동
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs구현
# procedure ftn
def bfs():
    '''
    x,y : 백조좌표
    nx,ny : 새좌표(사방으로 이동)
    c : 방문 기록
    a : 연못
    q : bfs를 위한 큐
    qtemp : 다음 bfs의 시작 큐
    :return: 완료여부
    '''
    while q:
        x,y = q.popleft()
        # 백조와 만나면 종료
        if x == x2 and y == y2:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바운더리 안이고
            if 0 <= nx < m and 0 <= ny <n:
                # 방문 한적이 없고
                if not c[nx][ny]:
                    # 물이면
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = True
    return False

# 얼음을 녹일때도 bfs
# also procedure
def melt():
    while wq:
        x, y = wq.popleft()
        # 얼음 꺠주기
        if a[x][y] == 'X':
            a[x][y] = '.'
        # 인접 영역들
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0 <= ny < n:
                #w에도 방문기록을 쓴다...
                if not wc[nx][ny]:
                    # 인접 얼음이면 임시큐에
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny])

                    #얼음아니면 탐색
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = True

# 입력
m, n  = map(int, input().split())
# 초기화
c = [[False]*n for _ in range(m)]
wc = [[False]*n for _ in range(m)]

a, swan = [], []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

#입력 호수 처리
for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j,k in enumerate(row):
            if a[i][j] == 'L':
                # + 연산...
                swan.extend([i,j])
                wq.append([i,j])
            elif a[i][j] == '.':
                wc[i][j] = True
                wq.append([i,j])

x1, y1, x2, y2 = swan
#시작점 넣음
q.append([x1,y1])
# 백조있는 공간은 물처리
a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', True
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq  = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1




