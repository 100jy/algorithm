#전체 그래프를 초기화

a = [[0,2,5,1,float('inf'),float('inf')],
     [2,0,3,2,float('inf'),float('inf')],
     [5,3,0,3,1,5],
     [1,2,3,0,1,float('inf')],
     [float('inf'),float('inf'),1,1,0,2],
     [float('inf'),float('inf'),5,float('inf'),2,0]]

number = len(a)

#방문여부 확인
v = [False]*6
#거리저장 배열
d = [0]*6

#가장 최소거리를 가지는 노드를 반환
#(방문하지 않은 노드중)
def getSmallIndex():
    min = 10**10
    index = 0
    #선형 탐색 방법(쉽지만 비용이 크다)
    for i in range(number):
        if d[i] < min and not(v[i]):
            min = d[i]
            index = i
    return index

# 다익스트라를 수행하는 함수
def dijkstra(start):
    #각 노드까지 직선 거리 가져온다
    for i in range(number):
        d[i] = a[start][i]
    #시작노드를 방문처리 한다
    v[start] =True

    #최소비용 노드 순으로 차례로 확인한다.
    for i in range(number - 2):
        current = getSmallIndex()
        v[current] = True
        for j in range(6):
            if not(v[j]):
                #current 노드를 거쳐서 가는 비용이 작다면
                if d[current] + a[current][j] < d[j]:
                    d[j] = d[current] + a[current][j]

if __name__ == '__main__':
    dijkstra(0)
    print(d)


#노드의 개수가 많은 데 노드간의 연결이 적은 경우 손해가 크다...
