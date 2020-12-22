T = int(input())

for i in range(T):
    tmp = ''
    n,string = input().split()
    n = int(n)

    for j in string:
        tmp += j*n

    print(tmp)
