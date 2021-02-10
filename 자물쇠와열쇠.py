def solution(key, lock):
    answer = False
    # 키를 돌리고 이동 시켜서
    # lock의 홈에 맞추어여함

    M = len(lock)
    N = len(key)

    # 키 좌표 구해주기
    key_axis = []
    for i in range(N):
        for j in range(N):
            if key[i][j]:
                key_axis.append((i,j))

    # 홈 좌표구해주기
    hole_axis = []
    for i in range(M):
        for j in range(M):
            if not(lock[i][j]):
                hole_axis.append((i,j))

    # 로테이트 구현
    def rotate(x, y, degree, n=N):

        if degree == 90:
            x, y = y, n-1-x
        elif degree == 180:
            x, y = y, x
        elif degree == 270:
            x, y = n-1-y, x
        else:
            return x, y

        return x, y


    for degree in [90,180,270,360]:
        for v in range(-(N-1), M):
            for h in range(-(N-1), M):
                holes = len(hole_axis)
                rest_keys = []
                for axis in key_axis:
                    x, y = axis
                    # 회전이동
                    x_new, y_new = rotate(x, y, degree)
                    # 0 ~ n-m 좌우상하로 키좌표이동
                    x_new, y_new = x_new + h, y_new + v
                    # 홈과 키좌표 다같고
                    if (x_new, y_new) in hole_axis:
                        holes-=1
                    else:
                        rest_keys.append((x_new, y_new))
                # 키가 다있으면
                if holes == 0 :
                    # 남는키가 없거나 전부 범위밖이면
                    if rest_keys == []:
                        return True
                    for rest_key in rest_keys:
                        x, y = rest_key
                        # 안맞는 키있으면 다음 탐색
                        if 0<=x<M and 0<=y<M:
                            break
                        return True

    return answer

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])