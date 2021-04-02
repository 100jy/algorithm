# 활성 비활성
# 초기는 비활성
# 활성만 상하좌우 동시 복제(퍼진다) (1초)
# M개를 활성상태로
# NxN 빈칸 벽 바이러스
# 활성이 비활성 칸으로 가면 활성으로 변한다
# 0빈칸 1벽 2바이러스

# 모든 빈칸에 바이러스가 퍼지는 최소시간

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def get_input():
    N, M = map(int, input().split())
    num_empty = 0
    board = [[0] * N for _ in range(N)]
    virus = []
    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)
            if int(cont) == 2:
                virus.append((i,j))
            elif int(cont) == 0:
                num_empty += 1

    return N, M, board, virus, num_empty


# 조합으로 M개 가지는 조합 저장
def get_comb(virus):
    return combinations(virus, M)

def bfs(active, num_empty):
    q = deque([])
    visit = [[False] * N for _ in range(N)]
    cnt = 0

    for x, y in active:
        q.append((x, y, 0))
        visit[x][y] = True

    while q:
        x, y, s = q.popleft()

        for dx, dy in [(1,0), (-1,0), (0,-1), (0, 1)]:
            new_x, new_y = x+dx, y+dy

            if 0<=new_x<N and 0<=new_y<N:
                if not(visit[new_x][new_y]):
                    if board[new_x][new_y] != 1:
                        visit[new_x][new_y] = True


                        #비활성 바이러스인 경우
                        if board[new_x][new_y] == 2:
                            q.append((new_x, new_y, s + 1))

                        #빈칸인 경우
                        else:
                            cnt += 1
                            if num_empty == cnt:
                                return s+1
                            q.append((new_x, new_y, s+1))

    return -1




def main():
    global board
    global N
    global actives
    global M

    N, M, board, virus, num_empty = get_input()
    if num_empty == 0:
        print(0)
        return None
    # M개 바이러스 위치 선택해서
    actives = get_comb(virus)
    # BFS
    s = []

    for active in actives:
        answer = bfs(active, num_empty)
        if answer > -1:
            s.append(answer)

    try:
        print(min(s))
    except:
        print(-1)

    return None


if __name__ == '__main__':
    main()
