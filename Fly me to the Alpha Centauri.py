import math
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    s = y-x
    k = math.ceil(math.sqrt(s+1/4)-1/2)
    if k**2 < s:
        print(2*k)
    else:
        print(2 * k -1)





