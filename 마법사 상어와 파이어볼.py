# NxN 격자에서 M개의 파이어볼
# (r,c)에서 (m,d,s)
# 주문을 하면
# d으로 s 욺직이고
# 이동이 끝날때마다
# 하나로 합치고
# 4개로 나눈다
# 질량이 0이면 사라진다.

# 구하는 것
# 남아있는 파이어볼의 질량의 합

from collections import defaultdict
#입력
def get_input():
    N, M, K = map(int, input().split())
    balls = []
    for i in range(M):
        #r, c, m, s, d
        cont = list(map(int, input().split()))
        # 0 start
        cont[0] -= 1
        cont[1] -= 1
        balls.append(cont)
    return N, balls, K


def move(balls, N):
    board = defaultdict(list)
    # 8방
    d_xy = [(-1,0),(-1,1),(0,1),(1,1),
            (1,0),(1,-1),(0,-1),(-1,-1)]

    for r, c, m, s, d in balls:
        # d방향으로 s칸 이동
        # 행끝 열끝이 연결된것 처리
        new_r, new_c = (r + s*d_xy[d][0]) % N,\
                        (c + s*d_xy[d][1]) % N

        board[(new_r,new_c)].append((m, s, d))

    return board


def devide(board, N):
    #[(r,c,m,s,d),]
    new_balls = []
    # 같은 위치의 값들 뺴내고
    for axis, arr in board.items():
        m_add, s_add = 0, 0
        odd, even = 0, 0

        # 만약 2개이상 있다면
        if len(arr)>=2:
            length = len(arr)
            # 전부 뺴낸다
            while arr:
                m, s, d = arr.pop()
                m_add += m
                s_add += s
                # 짝수홀수 체크
                if d % 2:
                    odd += 1
                else:
                    even += 1

            # 4개의 파이어볼의 방향
            if odd == 0 or even == 0:
                d_arr = [0,2,4,6]
            else:
                d_arr = [1,3,5,7]

            # 뺴낸것들 4개로 나눠주기
            for i in range(4):
                # 뺀것들
                # 나누어서 넣어준다
                # 질량이 없을 시 소멸
                if m_add//5 > 0:
                    # r,c,m,s,d
                    new_balls.append((axis[0],
                                      axis[1],
                                      m_add//5,
                                        s_add//length,
                                        d_arr[i]))
        # 나누지 않는 다면 그대로 넣기
        else:
            m, s, d = arr.pop()
            new_balls.append((axis[0],
                              axis[1],
                              m, s, d))

    # 새로운 볼들
    return new_balls


def get_sum(balls):
    answer = 0
    for r,c,m,s,d in balls:
        answer += m
    return answer

def main():
    N, balls, K = get_input()

    for i in range(K):
        board = move(balls, N)
        balls = devide(board, N)

    return get_sum(balls)


if __name__ == '__main__':
    answer = main()
    print(answer)