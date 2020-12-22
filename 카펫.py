def solution(brown, yellow):
    answer = []
    import math

    def get_factor(n):
        fac = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                fac.append(i)
        print(fac)
        return fac

    fac = get_factor(yellow)

    def get(len_in):
        bro = len_in*2 + int(yellow / len_in)*2 + 4

        if bro == brown:
            if len_in+2 not in answer:
                answer.append(len_in + 2)
                answer.append(yellow / len_in + 2)
                answer.sort(reverse=True)

    for i in fac:
        get(i)

    return answer


solution(8,1)