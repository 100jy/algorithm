def solution(m, n, puddles):
    answer = 0
    c = [[0*x]*(n+1) for x in range(m+1)]

    # 최단경로의 개수
    # 그 다음 경로는 이전 경로 중에 최단거리에서 합
    def case(x, y):
        if x == 1 and y == 1:
            return 1

        elif c[x][y] != 0:
            return c[x][y]

        else:
            if [x, y] in puddles:
                return 0
            elif 1 < x and 1 < y:
                c[x][y] = case(x - 1, y) + case(x, y - 1)
            elif x == 1:
                c[x][y] = case(x, y - 1)
            elif y == 1:
                c[x][y] = case(x - 1, y)

        return c[x][y]

    answer = case(m, n) % 1000000007

    return answer