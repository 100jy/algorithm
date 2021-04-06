# N까지의 수열
# N-1개의 연산자 끼워 넣기


N = int(input())

nums = list(map(int, input().split()))

a, s, m, d = map(int, input().split())
total = {'+' :a, '-':s, '*':m, '//':d}


def DFS(d, val, dic, l):
    global min_val
    global max_val
    if d == N:
        if val < min_val:
            #print(l, val)
            min_val = val
        if val > max_val:
            #print(l, val)
            max_val = val
        return

    for i in ['+', '-', '*', '//']:
        if dic[i] + 1 <= total[i]:
            dic[i] += 1
            if i == '//' and (val<0):
                new_val = -1 * eval(str(max(val, -val)) +
                               i + str(nums[d]))
            else:
                new_val = eval(str(val) + i + str(nums[d]))
            DFS(d + 1, new_val, dic, l+[i])
            dic[i] -= 1


from collections import defaultdict
global min_val, max_val
min_val = float('inf')
max_val = -float('inf')
DFS(1, nums[0], defaultdict(int), [])
print(max_val)
print(min_val)