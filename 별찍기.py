# 배열로 접근..
## 별리 있을 경우 1, 아니면 0

n = int(input())

global arr
arr = [[0*x]*(3**8) for x in range(3**8)]


def star(k, x, y):
    if k == 1:
        # 가장 작은 사각형
        global arr
        arr[x][y] = 1

    else:
        for i in range(3):
            for j in range(3):
                # 가운데는 비운다.
                if (i, j) != (1, 1):
                    star(k // 3, x + (k // 3) * i, y + (k // 3) * j)

star(n, 0, 0)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
