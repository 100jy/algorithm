# N명 짝수
# 팀나눔
# i번과 j번이 같은 팀에 있을떄 더해지는 능력
# sum(s)는 팁의 능력치

# 팀간의 차이 최소화

import sys
from itertools import combinations
input = sys.stdin.readline

def get_input():
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
    return N, board


def DFS(d, a, b, p, a_cnt, b_cnt):
    # 선수 다뽑거나
    # 다지나 쳤으면
    # 종료
    global min_sub
    if d == N:
        if a_cnt == N//2:
            if abs(a-b) < min_sub:
                min_sub = abs(a-b)
        return

    if a_cnt > N//2 or d-a_cnt > N//2:
        return

    for c in [True, False]:
        if c:
            new = (d, 1)
            new_a = a

            for idx, team in p:
                if team == 1:
                    new_a += board[d][idx] + board[idx][d]

            DFS(d+1, new_a, b, p + [new], a_cnt+1, b_cnt)

        else:
            new = (d, 0)
            new_b = b

            for idx, team in p:
                if team == 0:
                    new_b += board[d][idx] + board[idx][d]

            DFS(d + 1, a, new_b, p + [new], a_cnt, b_cnt+1)

    # 현재 명단이랑 시너지
    # 조회해서 합쳐줌
    # 뽑고 한뽑고로 다음 탐색

def main():
    global N, board
    N, board = get_input()
    global min_sub
    min_sub = float('inf')
    # N개중에 2개 선택
    DFS(0, 0, 0, [], 0, 0)
    print(min_sub)


if __name__ == '__main__':
    main()