# 다음 선분은 이전 세대를
# 전부를 시계방향 90
# 끝점에 붙여준다

# 좌표에서 그려주면서 좌표값 TRUE로 바꿔주기
# 끝점기준


import sys
from collections import deque, defaultdict
import math

input = sys.stdin.readline

def get_input():
    N = int(input())
    figure = []
    for i in range(N):
        x, y, d, g = \
            map(int, input().split())
        figure.append((x, y, d, g))

    return N, figure


def make_plot(x, y, d, g, points):

    dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    end_point = (x+dir[d][0], y+dir[d][1])
    p = deque([end_point, (x, y)])

    points[(x, y)] = 1
    points[end_point] = 1

    for g in range(g):
        a, b = end_point[0], end_point[1]
        new_p = deque([])
        cos = math.cos(math.pi/2)
        sin = math.sin(math.pi/2)

        for i, (x, y) in enumerate(p):
            if i == 0:
                continue
            new_x = ((x-a) * cos - (y-b) * sin)
            new_y = ((x-a) * sin + (y-b) * cos)
            new_point = (round(new_x + a), round(new_y + b))
            new_p.appendleft(new_point)
            points[new_point] = 1

        end_point = new_point
        p = new_p + p

    return points


def check_square(points):
    cnt = 0

    for x, y in points.keys():
        if (x+1,y) in points.keys()\
            and (x,y+1) in points.keys()\
                and (x+1,y+1) in points.keys():
                    cnt += 1

    return cnt

def main():
    N, figure = get_input()
    points = defaultdict(int)

    for x, y, d, g in figure:
        points = make_plot(x, y, d, g, points)

    num = check_square(points)

    print(num)


if __name__ == '__main__':
    main()