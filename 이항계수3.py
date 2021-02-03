########################풀이###########################
#

# 이항정리 : nCk = n-1Ck + n-1Ck-1

# 페르마의 소정리
# if p : prime # and
# a/p not in I
# a^(p-1) = 1 (mod p)
# a^(p-1)을 p로 나눈 나머지는 1이다.
# 주어진 1e9+7은 prime # so use 페르마의 소정리
# from A^(p-1) = 1 (mod p)
# A*A^(p-2) = 1 (mod p)
# A^(p-2) = A^(-1) (mod p)
# for nCk % p = [n!/((n-k)!k!)] % p
# = (n! % p) * [(n-k)!^(p-2) % p] * [(k)!^(p-2) % p]
#####################################################


####################제곱연산 분할정복###################
# 분할정복이용하면 O(logn)의 시간으로 계산가능
#Binary exponentiation
# 이진법이용 거듭제곱 계산
# 3^13 = 3^(1101_2) = 3^8 * 3^4 * 3*1
# a^n =
# 1 if n==0,
# (a*(n/2))^2 if n is even,
# (a*((n-1)/2))^2 * a o.w.
'''
def pow(a,b):
    res = 1
    while b>0:
        if b % 2:
            res *= a
        a = a * a
        b //= 2

    return res
'''
######################################################


# 입력처리
import sys

input =sys.stdin.readline

N, K = map(int, input().split())
P = 1000000007


def pow(a,b):
    res = 1
    while b>0:
        if b % 2:
            # 미리나눠놓기
            res *= a
            res %= P

        a = a * a
        a %= P
        b //= 2

    return res


if __name__ == '__main__':
    fac = [1] * 4000001
    inv = [1] * 4000001
    # 동적프로그래밍
    for i in range(1, 4000001):
        # 미리 나누어 놓기
        fac[i] = (i*fac[i-1]) % P

    #페르마의 소정리
    inv[4000000] = pow(fac[4000000], P-2)
    # 1/A! = (A+1) * 1/(A+1)!
    for i in range(4000000-1, 0, -1):
        inv[i] = (inv[i+1]*(i+1)) % P

    if (N == K) or (K==0):
        print(1)

    else:
        r = (fac[N]*inv[N-K]) % P
        r = (r*inv[K]) % P
        print(r)
