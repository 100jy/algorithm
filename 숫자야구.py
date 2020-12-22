global cnt
cnt = 0


def solution(baseball):

    # 몇스트, 몇볼인지
    def get(call, real):
        st = 0
        ball = 0
        a_s = str(call)
        b_s = str(real)
        for k in range(3):
            if a_s[k] == b_s[k]:
                st += 1
            elif a_s[k] in b_s:
                ball += 1
        return [st,ball]

    def get_num(arr, n, k):
        if k == len(arr):
            global cnt
            cnt += 1
            return

        # a스트,b볼 아니면 return
        sb = get(arr[k][0], n)
        if sb != arr[k][1:]:
            return

        get_num(arr, n, k + 1)

    for i in range(1,10):
        for t in range(1,10):
            if t != i:
                for p in range(1,10):
                    if p != t and p != i:
                        print(int(str(i)+str(t)+str(p)))
                        get_num(baseball, int(str(i)+str(t)+str(p)), 0)


    answer = cnt

    return answer