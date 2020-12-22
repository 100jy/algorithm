def solution(N, number):
    # (N,k) array를 만들고 계속 활용해야함

    array = [0] * 9
    array[0] = [N]
    oper = ['//', '*', '+', '-']

    def com(k, n, string):
        if k == n:
            global arr
            if eval(string) not in arr:
                arr.append(eval(string))
            return

        if k == 0:
            new_string = string + str(N)
            com(k + 1, n, new_string)

        else:
            for i in oper + ['']:
                new_string = string + i + str(N)
                com(k + 1, n, new_string)

    def inter(a, b):
        temp = []
        for i in a:
            for j in b:
                for p in oper:
                    if j !=0 and oper !='//':
                        val = eval(str(i) + p + str(j))
                        if val not in temp:
                            temp.append(val)
        return temp

    def get(k):
        if array[k] == 0:
            global arr
            arr = []
            com(0, k, '')

            if k % 2 == 0:
                t = k - 1
                while t == k / 2:
                    arr += inter(get(t), get(k - t))
                    t -= 1

            else:
                t = k - 1
                while t > (k / 2):
                    arr += inter(get(t), get(k - t))
                    t -= 1

            array[k] = arr

        else:
            return array[k]

        return array[k]


    k = 0
    while True:
        if k >8 :
            answer = -1
            break
        tmp = get(k)
        if number in tmp:
            break
        k += 1
        answer = k

    return answer