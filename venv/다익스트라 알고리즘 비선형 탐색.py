# 우선순위 규를 이용하여 최소 비용을 빠르게 탐색

import heapq

inf = float('inf')
number = 6


def dijkstra(start):
    d[start] = 0
    pq = []
    heapq.heappush(pq,(0,start))

    while len(pq) != 0:
        #하나씩 가져온다.
        #최소비용의 노드를 가져온다
        current = pq[0][1]
        #선탠된 노드까지 가는 비용
        distance = pq[0][0]
        heapq.heappop(pq)
        # 짧은 경우가 아닐 경우 넘어 가겠다.
        if d[current] < distance :
            continue

        for i in range(len(a[current])):
            #선택된 노드의 인접노드
            next = a[current][i][0]
            #선택된 노드를 거친 인접노드까지 거리
            nextDistance = distance + a[current][i][1]
            #거치는 것이 더 짧다면 갱신

            if nextDistance < d[next]:
                d[next] = nextDistance
                #새로운 짧은 노드에서 다시 반복...
                heapq.heappush(pq,(nextDistance,next))

if __name__ == '__main__':
    d = [inf] * 7
    a,b,c,g,e,f = [[],[],[],[],[],[]]

    heapq.heappush(a, (2, 2))
    heapq.heappush(a, (3, 5))
    heapq.heappush(a, (4, 1))

    heapq.heappush(b, (1, 2))
    heapq.heappush(b, (3, 3))
    heapq.heappush(b, (4, 2))

    heapq.heappush(c, (1, 5))
    heapq.heappush(c, (2, 3))
    heapq.heappush(c, (4, 3))
    heapq.heappush(c, (5, 1))
    heapq.heappush(c, (6, 5))

    heapq.heappush(g, (1, 1))
    heapq.heappush(g, (2, 2))
    heapq.heappush(g, (3, 3))
    heapq.heappush(g, (5, 1))

    heapq.heappush(e, (3, 1))
    heapq.heappush(e, (4, 1))
    heapq.heappush(e, (6, 2))

    heapq.heappush(f, (3, 5))
    heapq.heappush(f, (5, 2))

    a = [[],a,b,c,g,e,f]

    dijkstra(1)
    del d[0]
    print(d)














