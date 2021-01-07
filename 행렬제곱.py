######################################
#행렬의 제곱문제
# NxN 행렬을 B번 거듭제곱한 결과
# mod 1000
######################################

######################################
# 빠른 거듭제곱
# binary exponential
# b/2 만큼만 반복 돈다

def power(a, b):
    res = 1
    while b>0:
        #짝수의 경우
        if b%2:
            res *= a
        a = a * a
        b //= 2
    return res
######################################

import sys

def matrix_mutiply(a,b):
    n = len(a)
    c = [[0] * n for x in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= 1000
    return c

def mat_pow(a,b):
    n = len(a)
    res = [[0] * n for x in range(n)]
    for i in range(n):
        res[i][i] = 1

    while b>0:
        if b%2:
            res = matrix_mutiply(res,a)
        a = matrix_mutiply(a,a)
        b //= 2

    return res

n,b =map(int, input().split())
arr = []

for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    arr.append(line)

result = mat_pow(arr, b)
for i in range(n):
    for j in range(n):
        print(result[i][j])


