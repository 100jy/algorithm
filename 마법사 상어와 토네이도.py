#설멸
# NxN 격자
# 중앙에서 출발하여 반시계 방향으로 토네이도
# 0,0 에서 멈춤
# 주변으로 모래 흩날림


# 구하는것
# 토네이도 이동 마치고 격자밖으로 이동한 양


#입력

def get_input():
    N = int(input())
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        line = input().split()
        for j,cont in enumerate(line):
            board[i][j] = int(cont)

    return board


def blow(board, axis, d):
    x, y = axis
    # 흩날릴 모래
    sand = board[x][y]
    out_mount = 0
    # 위
    # 배열로 맵핑
    # [((x, y), val)]
    rest = (sand-(2*int(sand*(2/100)) +
                  2* int(sand*(7/100))+
                  2*int(sand*(10/100))+
                  2*int(sand*(1/100))+
                  int(sand*(5/100))))

    L_pattern = [
        # 2%
        ((x-2,y),int(sand*(2/100))),
        ((x+2,y),int(sand*(2/100))),
        # 7%
        ((x-1,y),int(sand*(7/100))),
        ((x+1,y),int(sand*(7/100))),
        # 10%
        ((x-1,y-1),int(sand*(10/100))),
        ((x+1,y-1),int(sand*(10/100))),
        # 1%
        ((x-1,y+1),int(sand*(1/100))),
        ((x+1,y+1),int(sand*(1/100))),
        # 5%
        ((x,y-2),int(sand*(5/100))),
        # A
        ((x,y-1), rest)]

    R_pattern = [
        # 2%
        ((x-2,y),int(sand*(2/100))),
        ((x+2,y),int(sand*(2/100))),
        # 7%
        ((x-1,y),int(sand*(7/100))),
        ((x+1,y),int(sand*(7/100))),
        # 10%
        ((x-1,y+1),int(sand*(10/100))),
        ((x+1,y+1),int(sand*(10/100))),
        # 1%
        ((x-1,y-1),int(sand*(1/100))),
        ((x+1,y-1),int(sand*(1/100))),
        # 5%
        ((x, y+2),int(sand*(5/100))),
        # A
        ((x,y+1), rest)]

    U_pattern = [
        # 2%
        ((x,y-2),int(sand*(2/100))),
        ((x,y+2),int(sand*(2/100))),
        # 7%
        ((x,y-1),int(sand*(7/100))),
        ((x,y+1),int(sand*(7/100))),
        # 10%
        ((x-1,y-1),int(sand*(10/100))),
        ((x-1,y+1),int(sand*(10/100))),
        # 1%
        ((x+1,y+1),int(sand*(1/100))),
        ((x+1,y-1),int(sand*(1/100))),
        # 5%
        ((x-2, y),int(sand*(5/100))),
        # A
        ((x-1,y), rest)]

    D_pattern = [
        # 2%
        ((x,y-2),int(sand*(2/100))),
        ((x,y+2),int(sand*(2/100))),
        # 7%
        ((x,y-1),int(sand*(7/100))),
        ((x,y+1),int(sand*(7/100))),
        # 10%
        ((x+1,y-1),int(sand*(10/100))),
        ((x+1,y+1),int(sand*(10/100))),
        # 1%
        ((x-1,y+1),int(sand*(1/100))),
        ((x-1,y-1),int(sand*(1/100))),
        # 5%
        ((x+2, y),int(sand*(5/100))),
        # A
        ((x+1, y), rest)]

    pattern = {'L':L_pattern,
               'U':U_pattern,
               'D':D_pattern,
               'R':R_pattern,
               }

    # 모래 비워주고
    board[x][y] = 0

    # 분배함
    for m in pattern[d]:
        (a, b), addm = m
        if 0<=a<len(board) and 0<=b<len(board):
            board[a][b] += addm
        else:
            # 나갈 경우 더해준다.
            out_mount += addm

    return board, out_mount


def get_next(axis, k, cnt):
    # k : 짝 홀
    # 짝낮 0 짝높1 홀낮 2 홀높3
    index = 2*(k % 2) + int(cnt >= k)
    pattern = ['R', 'U', 'L', 'D']
    daxis = [(0,1),(-1,0),(0,-1),(1,0)]
    d = pattern[index]
    x, y = daxis[index]
    next_axis = (axis[0]+x, axis[1]+y)
    return next_axis, d


# 이동 패턴
# 좌1 하1 우2 상2 좌3 하3 우4
# L D R R U U
def main(board):
    suma = 0
    # 중앙에서 시작
    axis = (len(board)//2, len(board)//2)
    k = 1
    cnt = 0

    while True:
        # 패턴대로 이동하고
        axis, d = get_next(axis, k, cnt)
        # 한번 이동 떄마다 모래 날리기
        board, out_mount = blow(board, axis, d)
        # 나간 모래 더해주고
        suma += out_mount
        # 좌표구하기 위해
        cnt += 1
        # 2k번 하면
        # 차수 늘리고 새로 카운트
        if cnt == 2*k:
            cnt = 0
            k += 1

        # 좌표 0,0에 도달하며 종료
        if axis == (0,0):
            return suma

if __name__ == '__main__':
    board = get_input()
    answer = main(board)
    print(answer)