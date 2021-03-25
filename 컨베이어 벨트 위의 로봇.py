# N 길이 벨트 위아래로 두개의 벨트가 돌고 있음
# 시계 방향 회전
# 내구도 있음
# 로봇은 1번에서 올라가고 N번 위치에서 내려감
# 내려가는 위치에서는 반드시 내려감
# 내구도 0인칸에는 못올라감

# 로봇을 모두 건너편으로 옮기길 원함


def get_input():
    N, K = map(int, input().split())
    du = map(int, input().split())
    belt = []
    for d in du:
        belt.append((False, d))
    return N, K, belt

def run(belt):
    return [belt[-1]] + belt[:-1]


def load(belt, N):
    #이동

    for id, (r, d) in enumerate(belt[:N][::-1]):
        id = N-1-id
        # 로봇이 적재되어 있다면
        if r:
            # 내리는 곳이라면 내려주기
            if id == N-1:
                belt[id] = (False, belt[id][1])
            else:
                # 조건 만족하면
                if not(belt[id+1][0]) and belt[id+1][1] > 0:
                    # 내린다면
                    if id+1 == N-1:
                        belt[id] = (False, belt[id][1])
                        belt[id+1] = (False, belt[id+1][1]-1)

                    else:
                        # 한칸이동
                        # 내구도 감소
                        belt[id+1] = (True, belt[id+1][1]-1)
                        belt[id] = (False, belt[id][1])

    # 적재
    if belt[0][1] > 0:
        # 적재하고
        #내구도 감소
        belt[0] = (True, belt[0][1]-1)

    return belt


def check(belt, K):
    # 내구도가 0인칸 K개 이상이면 종료
    suma = 0
    for _, d in belt:
        if d == 0:
            suma += 1

    return suma >= K



def main():
    N, K, belt  = get_input()
    cnt = 0

    while True:
        cnt+=1
        # 벨트 회전시키고
        belt = run(belt)
        # 이동 시키고
        # 로봇적재하고
        belt = load(belt, N)
        # 종료검사
        if check(belt, K):
            break

    return cnt

if __name__ == '__main__':
    answer = main()
    print(answer)