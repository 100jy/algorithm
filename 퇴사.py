# 남은 N일 동안
# 최대한 많은 상담
# 하루에 하나씩 상담
# 상담을 했을 때 최대이익

import sys
input = sys.stdin.readline


def get_input():
    N = int(input())
    calls = []
    for i in range(N):
        T, P = map(int, input().split())
        calls.append((T,P))

    return N, calls


def DFS(N, calls, s, t, a, visit):
    global max_s
    if t >= N:
        if t == N:
            a = 0
        if (s-a) > max_s:
            max_s = (s-a)

        return

    # 선택
    if not(visit[t]):
        visit[t] = True
        DFS(N, calls, s+calls[t][1], t+calls[t][0], calls[t][1],
            visit)
        visit[t] = False
    #선택안함
    DFS(N, calls, s, t + 1, 0, visit)


def main():
    global N
    N, calls = get_input()
    global max_s
    max_s = -float('inf')
    # DFS 돌면서
    DFS(N, calls, 0, 0, 0, [False] * N)

    print(max_s)


if __name__ == '__main__':
    main()