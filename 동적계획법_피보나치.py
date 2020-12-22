# 이렇게 하면 매우 느리다....
def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    return dp(n -1) + dp(n -2)


#이미 구한 값은 안구하게 만들어 준다...
# 메모이제이션..., 시간이 많이 줄어든다.
global arr
arr = [0]*100

def dp_n(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    elif arr[n] != 0:
        return arr[n]

    else:
        arr[n] = dp(n - 1) + dp(n - 2)

    return arr[n]

print(dp_n(30))