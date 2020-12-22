import math
import time
start = time.time()

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def get_prime(n):
    #조건에 해당 될 시에만 저장
    arr = [x for x in range(1,n+1) if is_prime(x)]
    return arr

get_prime(10**5)

print(time.time() - start)