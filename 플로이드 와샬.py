number  = 4
inf = float('inf')

#배열을 초기화
a = [[0,5,inf,8],
     [7,0,9,inf],
     [2,inf,0,4],
     [inf,inf,3,0]]


def floydWarshall():
    #결과 배열 초기화
    d = [x for x in a]
    # k = (거쳐가는 노드)
    for k in range(number):
        #출발노드 i, 도착노드 j
        for i in range(number):
            for j in range(number):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

    return d


if __name__ == '__main__':
    tmp = floydWarshall()
    print(tmp)


