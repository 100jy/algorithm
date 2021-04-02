# NxN
# 모든 칸에 초기 양분 5
# 로봇이 조사
# M개의 나무


# k년 후에 남은 나무개수

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def get_input():
    N, M, K = map(int, input().split())
    trees = defaultdict(deque)
    ground = [[5] * N for _ in range(N)]
    A = defaultdict(int)

    for i in range(N):
        line = input().split()
        for j, cont in enumerate(line):
            A[(i,j)] = int(cont)

    for i in range(M):
        x,y,z = map(int, input().split())
        trees[(x-1, y-1)].append(z)

    return N, M, K, A, trees, ground


def spring_summer_fall(trees):
    # 봄
    # 나이만큼 양분 먹음
    new_trees = defaultdict(deque)

    d = [(-1, -1), (-1, 0), (0, -1), (1, -1),
         (1, 1), (1, 0), (0, 1), (-1, 1)]
    cnt = 0
    for (x, y), ages in trees.items():
        now_amt = ground[x][y]
        while ages:
            age = ages.popleft()
            # 된다면
            if now_amt-age >= 0:
                ground[x][y] -= age
                now_amt -= age
                # 나이 1증가
                new_trees[(x, y)].append(age+1)
                cnt += 1

                #가을
                # 나이가 5의 배수인 나무
                if (age+1) % 5 == 0:
                    # 8방위에 나이가 1인나무 생성
                    for dx, dy in d:
                        if 0 <= x + dx < N and 0 <= y + dy < N:
                            new_trees[(x + dx , y + dy)].appendleft(1)
                            cnt += 1

            # 죽는다면
            else:
                # 여름
                # 봄에 죽은 나무가 양분으로
                ground[x][y] += age // 2

    return new_trees, cnt


def winter():
    # 겨울
    # 양분 추가
    for (x, y), addm in A.items():
        ground[x][y] += addm

    return None


def main():
    global N
    global M
    global K
    global A
    global trees
    global ground

    N, M, K, A, trees, ground = \
        get_input()

    for i in range(K):
        trees, cnt = spring_summer_fall(trees)
        winter()

    print(cnt)

if __name__ == '__main__':
    main()



