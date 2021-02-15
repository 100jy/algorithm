# 다익스트라 알고리즘
# 2차원 배열과 힙이용
# 각 노드를 거치는 경우 더 싸지면 비용을 갱신
# 최종 배열은 i에서 j로 가는 최저 비용이 된다

# K지점에서 갈라진다는 가정하에
# 비용 (s부터 k 요금) + (k부터 a 요금) + (k부터 b 요금)
# k를 전부 s 뺴고 전부 가정하여 요금 계산

import heapq
def solution(n, s, a, b, fares):
    answer = float('inf')
    from collections import defaultdict
    graph = defaultdict(list)
    # (연결된 노드와 비용)
    for start, to, fare in fares:
        graph[start].append((to, fare))
        graph[to].append((start, fare))

    def dijkstra(n, s, graph):
        # 거리저장 (n칸)
        d = defaultdict(float)
        for i in graph.keys():
            d[i] = float('inf')
        pq = []
        # (비용, 노드)
        heapq.heappush(pq, (0, s))
        while pq:
            # 현재노드까지 비용과
            cost = pq[0][0]
            # 현재 노드
            current = pq[0][1]
            heapq.heappop(pq)
            # 거쳐서 비용이 줄어드는 경우만 탐색
            if d[current] < cost:
                continue
            # 각 경로까지 선택된 노드 거칠 경우 탐색
            for i in range(len(graph[current])):
                # 현재 노드에서 연결된 노드와
                next = graph[current][i][0]
                # 새로운 비용
                new_cost = graph[current][i][1] + cost

                # 더 저렴해지는 경우만 갱신
                if new_cost < d[next]:
                    d[next] = new_cost
                    # 새로운 최저에서 탐색
                    heapq.heappush(pq,(new_cost, next))

        return d

    d = dijkstra(n, s, graph)

    for k in graph.keys():
        if k == s:
            cost_a = dijkstra(n, k, graph)[a]
            cost_b = dijkstra(n, k, graph)[b]
            cost_k = 0
        elif k == a:
            cost_a = 0
            cost_b = dijkstra(n, k, graph)[b]
            cost_k = dijkstra(n, s, graph)[k]
        elif k == b:
            cost_a = dijkstra(n, k, graph)[a]
            cost_b = 0
            cost_k =  dijkstra(n, s, graph)[k]
        else:
            cost_a = dijkstra(n, k, graph)[a]
            cost_b = dijkstra(n, k, graph)[b]
            cost_k = dijkstra(n, s, graph)[k]

        cost = cost_k + cost_a + cost_b

        if cost<answer:
            answer = cost

    return answer

solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]])