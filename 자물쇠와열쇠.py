def solution(key, lock):
    answer = True
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
            x, y = y, n-x
        elif degree == 180:
            x, y = y, x
        elif degree == 270:
            x, y = n-y, x
        else:
            return x, y

        return x, y

    for degree in [90,180,270,360]:
        for v in range(-(N-1), M):
            for h in range(-(N-1), M):
                for axis in key_axis:
                    x, y = axis
                    # 회전이동
                    x_new, y_new = rotate(x, y, degree)
                    # 0 ~ n-m 좌우상하로 키좌표이동
                    x_new, y_new = x_new + v, y_new + h
                    # 홈과 키좌표 다같고
                    hole_axis
                    # 남는키가 범위내에 있다면
                    # 트루

    return answer

