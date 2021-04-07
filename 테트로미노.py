import sys
input = sys.stdin.readline


def get_input():
    N, M = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)

    return N, M, board


def DFS(s, d, x, y):
    # 시작점에서 4방으로 1칸씩 뽑고
    # 4칸이 되면 종료
    global max_sum, visit
    if d == 4:
        if s > max_sum:
            max_sum = s
        return

    for dx, dy in [(1, 0), (-1, 0),
                   (0, 1), (0,-1)]:

        a, b = x+dx, y+dy
        if 0<=a<N and 0<=b<M:
            if not(visit[a][b]):
                visit[a][b] = True
                DFS(s+board[a][b], d+1, a, b)
                visit[a][b] = False


def check(x, y):
    s = board[x][y]
    cnt = 0
    ch = 1
    val = []
    for dx, dy in [(1, 0), (-1, 0),
                   (0, 1), (0, -1)]:
        if 0<=x+dx<N and 0<=y+dy<M:
            val.append(board[x+dx][y+dy])
            s += board[x+dx][y+dy]
            ch += 1

        # 4개 이하면 리젝
        else:
            cnt+=1
            if cnt>=2:
                return 0

    # 4개면 가장 작은 거하나뺸다
    if ch == 5:
        s -= min(val)

    global max_sum
    if s > max_sum:
        max_sum = s

    return

def main():
    global N, M, board
    N, M, board = get_input()

    global max_sum, visit
    max_sum = 0
    visit = [[False] * M for _ in range(N)]

    # 연결된 4칸 합중 최대???
    for i in range(N):
        for j in range(M):
            visit[i][j] = True
            DFS(0, 0, i, j)
            visit[i][j] = False
            check(i, j)

    print(max_sum)


if __name__ == '__main__':
    main()