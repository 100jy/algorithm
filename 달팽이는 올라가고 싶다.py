import math
a, b, v = list(map(int,input().split()))
step = a - b
print(math.ceil((v-a)/step + 1))