# N x N 빈칸, 치킨집, 집중하나
# 치킨거리는 가장 가까운 치킨집까지의 거리
# 도시의 치킨거리는 치키거리들의 합

# M개만 골라서
# 치킨거리들의 합이 최소가 되게

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def get_input():
    N, M  = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    house = []
    chicken = []

    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)
            if cont == '1':
                house.append((i,j))
            elif cont == '2':
                chicken.append((i,j))

    return N, M, board, house, chicken


def get_comb(chicken, M):
    return combinations(chicken, M)


def get_shortest(h, chick):
    min_dist = float('inf')
    for x, y in chick:
        dist = abs(h[0] - x) + abs(h[1] - y)
        if dist < min_dist:
            min_dist = dist
    return min_dist


def main():
    N, M, board, house, chicken =\
        get_input()

    # NCM개 치킨집구하고
    comb = get_comb(chicken, M)
    min_dist = float('inf')

    for chick in comb:
        dist = 0
        # 해당 치킨 중에서 최단거리 구하고
        for h in house:
            dist += get_shortest(h, chick)
        if dist < min_dist:
            min_dist = dist

    print(min_dist)


if __name__ == '__main__':
    main()

