# N개의 시험장
# 응시자수 A명,
# 총은 B명 부는 C명
# 총은 1명만
# 필요한 최소 감독관수는

import math

def get_input():
    N = int(input())

    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    return A, B, C


def main():
    A, B, C = get_input()
    re = 0
    for num in A:
        if num < B:
            re+=1
        else:
            re += math.ceil((num - B) / C) + 1
    print(re)

if __name__ == '__main__':
    main()