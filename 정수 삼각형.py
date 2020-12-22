def solution(triangle):
    N = len(triangle)
    global arr
    arr = [[-1] * x for x in range(1, N + 1)]

    def get(k, i):

        if k == 0:
            arr[0][0] = triangle[0][0]

        if arr[k][i] != -1:
            return arr[k][i]

        else:
            if i == 0:
                arr[k][i] = get(k - 1, i) + triangle[k][i]
            elif i == k:
                arr[k][i] = get(k - 1, i - 1) + triangle[k][i]
            else:
                arr[k][i] = max(get(k - 1, i), get(k - 1, i - 1)) + triangle[k][i]

            return arr[k][i]

    for i in range(N):
        get(N-1, i)

    answer = max(arr[N - 1])

    return answer


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
