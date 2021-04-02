# r,c 격자
# 상어는 크기와 속도를 가짐
# 땅위에서
# 반대편 끝에서 종료

# 매초마다
# 낚시왕이 오른쪽으로 한칸이동
# 해당열에서 가장 땅에 가까운 상어 잡음
# 상어가 이동

# 상어 방향으로 속고 만큼이동
# 벽만난 경우 반대방향으로 속도만큼
# 상어가 이동을 마친 후에 같은 칸에 두명이면
# 큰 상어가 나머지를 모두 잡아먹음

# 마지막에 잡은 상어의 크기의 합

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

def get_input():
    R, C, M = map(int, input().split())
    water = defaultdict(list)
    for i in range(M):
        r, c, s, d, z = \
            map(int, input().split())

        # 해당 열에 정보추가
        # 깊이, 속력, 방향, 크기
        heapq.heappush(water[c-1], (r-1, s, d, z))

    return R, C, M, water


def fishing(c, water):
    # 있을 시에 낚는다.
    try:
        _, _, _, z = water[c].pop(0)
    except:
        z = 0
    return z


def move(water):
    # 상어 방향으로 속고 만큼이동
    # 벽만난 경우 반대방향으로 속도만큼

    new_shark = defaultdict(list)
    new_water = defaultdict(list)
    for c, sharks in water.items():
        for shark in sharks:
            r, s, d, z = shark
            dir = [(-1, 0), (1, 0),
                   (0,1), (0,-1)]
            new_r, new_c = \
               r + s*dir[d-1][0], c + s*dir[d-1][1]

            #벽만나는 경우
            if new_r<0 or new_r>=R:
                tmp_r = r
                new_d = dir[d-1][0]
                # 한칸씩이동
                for i in range(s):
                    #벽에서 방향바꿈
                    if tmp_r+new_d < 0 or\
                            tmp_r+new_d > R-1:
                        new_d *= -1
                        d += new_d
                        tmp_r += new_d
                    else:
                        tmp_r += new_d
                new_r = tmp_r

            if new_c<0 or new_c>=C:
                tmp_c = c
                new_d = dir[d - 1][1]
                for i in range(s):
                    if tmp_c + new_d < 0 or \
                            tmp_c + new_d > C - 1:
                        new_d *= -1
                        d -= new_d
                        tmp_c += new_d
                    else:
                        tmp_c += new_d
                new_c = tmp_c

            # 이미 그칸에 상어있으면 큰 걸로 대체
            if new_shark[(new_c, new_r)]:
                # 무게가 더클떄만 추가
                if z > new_shark[(new_c, new_r)][-1]:
                    new_shark[(new_c, new_r)] = \
                        (s, d, z)
            else:
                new_shark[(new_c, new_r)] = \
                    (s, d, z)

    for (new_c, new_r), (s, d, z) in \
            new_shark.items():
        heapq.heappush(new_water[new_c], (new_r, s, d, z))

    return new_water


def main():
    global R
    global C
    global M

    R, C, M, water = get_input()
    bag = 0

    # 낚시꾼이동
    for c in range(C):
        # 낚시하고
        weight = fishing(c, water)
        bag += weight
        # 상어이동하고
        water = move(water)

    # 잡은 상어의 크기의 합
    print(bag)

    return None


if __name__ == '__main__':
    main()