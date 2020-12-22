# 컴파일 에러 예방, maxrecursion 확장
import sys
sys.setrecursionlimit(1100)
n = int(input())
arr = [0]*1001

#이미 구한 값은 기억해주어 반복을 줄인다.
def get(k):
    if k == 1:
        arr[1] = 1

    elif k == 2:
        arr[2] = 2

    elif arr[k] == 0:
        arr[k] = get(k-1) + get(k-2)

    return arr[k]

#modular 적용, 너무 길 경우
print(get(n)%10007)
