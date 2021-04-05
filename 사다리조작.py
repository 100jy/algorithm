# 세로선 N, 가로선 M
# 세로선 마다 최대 H개까지
# 선 놓을 수 있다.

# 가로선 연속해서는 안됨
# 가로선 접하면 안됨

# i번에서 i번으로 도착하기 위해
# 추가해야되는 세로선의 최솟값

import sys
input = sys.stdin.readline


def get_input():
    N, M, H =  map(int, input().split())
    h_line = [[False] * (N+1) for _ in range(H+1)]
    for i in range(M):
        a, b = map(int, input().split())
        # b 에서 b+1 으로 a번에서
        # h, v
        h_line[a][b] = True

    return N, M, H, h_line


# 선타기
# 가능한 조합들에서
def check(h_line, N, H):
    global run
    run = True
    chk = True
    # 세로줄 바꿔가며
    for v in range(1,N+1):
        c_v = v
        # 내려간다
        for h in range(1,H+1):
            if h_line[h][c_v]:
                # 세로줄 한칸 이동
                c_v += 1
            elif h_line[h][c_v-1]:
                c_v -= 1

        if c_v != v:
            return False

    # 전부 통과하면
    return chk


def DFS(n_h, a, b, h_line, d, H, N):

    # 원하는 결과 나오면
    # 그떄 숫자
    if d == n_h:
        if check(h_line, N, H):
            print(n_h)
            sys.exit()
        return

    # h, v
    i, j = a, b
    for a in range(i, H + 1):
        for b in range(1, N):
            if a == i:
                if b < j:
                    continue
            if not(h_line[a][b])\
                and not(h_line[a][b-1])\
                    and not(h_line[a][b+1]):
                h_line[a][b] = True
                DFS(n_h, a, b,  h_line, d+1, H, N)
                h_line[a][b] = False


def main():
    N, M, H, h_line = \
        get_input()
    # 가로선 개수 정하고
    n_h = 0
    while True:
        global result
        result = False

        global run
        run = False

        # 위치 옮겨가며 결과 만들기
        DFS(n_h, 0, 0, h_line, 0, H, N)

        if not run:
            print(-1)
            return

        n_h += 1
        # 3 초과하면 -1
        if n_h > 3:
            print(-1)
            return None


if __name__=='__main__':
    main()