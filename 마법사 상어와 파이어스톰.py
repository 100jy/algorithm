#설명
# 칸에 있는 것은 얼음 양
# L 단계 마법 시전하며 2**L x 2**L 칸 에서 90도 회전한후
# 인접한 칸에 얼음이 있는 칸이 3칸 이상 아니면 얼음 양이 1줄어듬

# 구하고자 하는것
# 남아있는 얼음의 합
# 남은 얼음 중 가장 큰 덩이의 칸 개수


# 입력
# N, Q
# 격자
# 주문 단계 수열

# 출력
# 첫줄 얼음 합
# 두줄 칸개수, 없으면 0


def get_input():
    # 입력처리
    N, Q = map(int, input().split())
    # 메모리 할당
    board = [[0] * (2**N) for _ in range(2**N)]
    for i in range(2**N):
        line = input().split()
        for j, cont in enumerate(line):
            board[i][j] = int(cont)
    # 주문 리스트
    spell = list(map(int, input().split()))
    return N, Q, board, spell

# 주어진 매트릭 격자내에서
# 90도 로데이트
def rotate(mat, L):
    length = 2 ** L
    new_mat = [[0] * len(mat) for _ in range(len(mat))]
    # 0 length**1 length**2 ...
    for start_i in range(len(mat)//length):
        start_i *= length
        for start_j in range(len(mat)//length):
            start_j *= length
            for i in range(length):
                for j in range(length):
                    new_mat[start_i + i][start_j + j] = \
                        mat[(length-1-j) + start_i][i + start_j]
    return new_mat

# 얼음 녹이기
# BFS
def check(mat):
    from collections import deque
    # 맨 위칸에서 출발
    q = deque([(0,0)])
    visit = [[False] * len(mat) for _ in range(len(mat))]
    visit[0][0] = True
    melt = []
    while q:
        # 새로운 탐색 좌표
        axis = q.popleft()
        cnt = 0
        # 인접을 탐색
        for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_x, new_y = axis[0] + x, axis[1] + y
            # 새좌표 영역안이고
            if (0<=new_x<len(mat)) and (0<=new_y<len(mat)):
                # 방문하지 않았다면
                if not(visit[new_x][new_y]):
                    # 방문대상에 추가
                    q.append((new_x, new_y))
                    visit[new_x][new_y] = True
                # 인근 영역 얼었는지 체크
                if mat[new_x][new_y] > 0:
                    cnt += 1
        # 만약 인근 3군데 이상 얼지 않았다면
        if cnt < 3:
            melt.append(axis)

    # 녹여주기
    for x, y in melt:
        mat[x][y] = max(0, mat[x][y] - 1)
    return mat

# 계산 후 남아있는 얼음의 양
def get_sum(mat):
    return sum(map(sum, mat))

# 가장 큰 덩이의 칸 개수
# BFS
def get_max_size(mat):
    from collections import deque
    def BFS(mat, x, y):
        # x, y에서 출발
        q = deque([(x,y)])
        visit = [[False] * len(mat) for _ in range(len(mat))]
        visit[x][y] = True
        size = 1
        while q:
            # 새로운 탐색 좌표
            axis = q.popleft()
            # 인접을 탐색
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_x, new_y = axis[0] + dx, axis[1] + dy
                # 새좌표 영역안이고
                if (0<=new_x<len(mat)) and (0<=new_y<len(mat)):
                    # 방문하지 않았다면
                    if not(visit[new_x][new_y]):
                        # 만약 얼어 있다면
                        if mat[new_x][new_y] > 0:
                            # 방문대상에 추가
                            q.append((new_x,new_y))
                            # 조검 만족하면 한칸 추가
                            size += 1
                            visit[new_x][new_y] = True

        # 탐색 마치면 사이즈 리턴
        return size

    # 모든 칸에서 시작해서 탐색
    # 그중 최댓값 선택
    size = [0]
    for i in range(len(mat)):
        for j in range(len(mat)):
            # 시작칸이 얼어있다면 탐색
            if mat[i][j] > 0:
                size.append(BFS(mat, i, j))

    return max(size)


def main():
    # 칸에 있는 것은 얼음 양
    # L 단계 마법 시전하며 2**L x 2**L 칸 에서 90도 회전한후
    # 인접한 칸에 얼음이 있는 칸이 3칸 이상 아니면 얼음 양이 1줄어듬

    N, Q, board, spell = get_input()

    # 주문 차례로 실행
    for L in spell:
        # 90도 회전하고
        board = rotate(board, L)
        # 얼음 녹이고
        board = check(board)

    suma = get_sum(board)
    m_size = get_max_size(board)

    return suma, m_size

if __name__ == '__main__':
    suma, m_size = main()
    print(suma)
    print(m_size)

