n = int(input())

import math

def is_prime(k):
    if k == 1:
        return False
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


for i in range(n):
    k = int(input())
    for j in range(int(k/2),k+1):
        if is_prime(j) and is_prime(k-j):
            print(k-j,j,sep=' ')
            break

