# 8개 톱니 가진 4종류의 톱니
# 톱니 N과 S 있음
# k번 반시계 혹은 시계회전


# K번 회전이후 점수 계산

import sys
from collections import deque
input = sys.stdin.readline

def get_input():
    gear = [[0]*8 for _ in range(4)]
    for i in range(4):
        line = input().split()
        for j, cont in enumerate(line[0]):
            gear[i][j] = int(cont)

    K = int(input())
    query = []
    for i in range(K):
        num, d = map(int, input().split())
        query.append((num, d))

    return K, gear, query


def move(gear, move_list):
    for q in move_list:
        num, d = q
        idx = num-1
        # idx번 기어 d 방향으로 회전
        # 시계
        if d==1:
            gear[idx] = [gear[idx][-1]] + gear[idx][:-1]
        # 반시계
        elif d==-1:
            gear[idx] = gear[idx][1:] + [gear[idx][0]]

    return gear

def BFS(gear, query):
    # DFS
    # 시작 기어에서 양옆으로 이동하며
    # 회전여부와 방향저장
    # 4개 다보면 중단
    q = deque([query])
    visit = [False] * 4

    visit[q[0][0]-1] = True
    result = []
    result.append(q[0])

    while q:
        num, d = q.popleft()
        for dx in [-1, 1]:
            if 1<=num+dx<=4:
                if not(visit[num+dx-1]) \
                    and ((gear[num-1][6] !=
                        gear[num+dx-1][2] and
                        dx == -1) or
                    (gear[num - 1][2] !=
                     gear[num + dx - 1][6] and
                     dx == 1)):
                    q.append((num+dx, -d))
                    result.append((num+dx, -d))
                    visit[num+dx-1] = True

    return result


def get_score(gear):
    score = 0
    if gear[0][0]:
        score += 1
    if gear[1][0]:
        score += 2
    if gear[2][0]:
        score += 4
    if gear[3][0]:
        score += 8

    return score


def main():
    K, gear, query = get_input()

    for q in query:
        move_list = BFS(gear, q)
        gear = move(gear, move_list)

    print(get_score(gear))


if __name__ == '__main__':
    main()