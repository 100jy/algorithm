number = 7
# 방문처리를 위한
c = [False] * 8
# index 저장
a = [[]] * 8

from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    c[start] = True
    while q:
        x = q[0]
        q.popleft()
        print(x)
        # 인접한 노드들을 큐에 넣어준다.
        for i in range(len(a[x])):
            y = a[x][i]
            if not (c[y]):
                q.append(y)
                c[y] = True


if __name__ == '__main__':
    a[1].append(2)
    a[2].append(1)

    a[1].append(3)
    a[3].append(1)

    a[2].append(3)
    a[3].append(2)

    a[2].append(4)
    a[4].append(2)

    a[2].append(5)
    a[5].append(2)

    a[3].append(6)
    a[6].append(3)

    a[4].append(5)
    a[5].append(4)

    a[6].append(7)
    a[7].append(6)

    bfs(1)
