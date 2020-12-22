# 배낭문제 , DP
# 점화식과 2차원 배열을 이용
# 재귀관계 찾기 -> 바텀업헤결 -> 이차원 배열 이용(메모라이제이션)


#######################################
# w: 제약조건, v: 최적화 대상, n: 매개변수

# P[i][j] : 총무게가 j를 초과 할 수 없다는
#           제략조건 하에서 처음 i개만 선택했을때 얻는 최적이익

# P[n][w] : n개의 아이템으로 얻는 최적이익, 최종적으로 얻고자하는 값

# P[i][w] = if w_i <= w, max(P[i-1][w], p_i + P[i-1][w-w_i])
#           (뺴고 새로운 걸 담거나 그대로 있거나)
#           elif w_i > w, P[i-1][w]
#           (넣을 수 없는 상황)

# 시간 복잡도는 배열의 크기(O(nW))
# 부르탈 포스의 경우(O(2^n))
# P[i][w]를 계산하려면 P[i-1][W], P[i-1][W-w_i]만 필요!!
#######################################


# 메인 함수
def DP(i, K, w, v, arr):

    if (i <= 0) or (K <= 0):
        return 0

    if arr[i][K]:
        return arr[i][K]

    #점화식
    # P[i-1][w]
    if w[i-1] > K:
        arr[i][K] = DP(i - 1, K, w, v, arr)
        return arr[i][K]

    # max(P[i-1][w], p_i + P[i-1][w-w_i])
    else:
        left = DP(i - 1, K, w, v, arr)
        right = v[i-1] + DP(i - 1, K - w[i-1], w, v, arr)
        arr[i][K] = max(left, right)
        return arr[i][K]

# 출력
if __name__ == '__main__':
    # 입력처리
    N, K = [int(x) for x in input().split(' ')]

    W = []
    V = []

    for i in range(N):
        w, v = [int(x) for x in input().split(' ')]
        W.append(w)
        V.append(v)

    arr = [[None] * (K+1) for x in range(N+1)]
    profit = DP(N, K, W, V, arr)
    print(profit)

############ review #############################
# index error 여러번 있었음
## 0부터 시작, 바깥 인덱스부터 접근([[]])
# 참고
## https://www.youtube.com/watch?v=A8nOpWRXQrs
# 파이참 디버깅 모드 도움 많이 됨!!
#################################################