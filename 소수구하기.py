import math


def is_prime(k):
    if k == 1:
        return False
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


start, end = list(map(int, input().split()))

for i in range(start, end+1):
    if is_prime(i):
        print(i)