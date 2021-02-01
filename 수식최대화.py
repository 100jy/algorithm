
def solution(expression):
    answer = 0
    # -, *, + 중에 우선순위 정해서 가장 큰값
    # 먼저 숫자 배열과 연산자 배열을 만들고
    # 6가지의 우선순위중 하나를 실행
    # 연산자를 하나씩없애가며 양옆의 숫자도 없앰
    # 2*3 + 6*2
    # 6 + 12
    sig, num = [],[]
    num_tmp = ''
    for s in expression:
        if s not in ['-', '*', '+']:
            num_tmp += s
        else:
            sig.append(s)
            num.append(int(num_tmp))
            num_tmp = ''
    num.append(int(num_tmp))


    mods = [('-', '*', '+'),
           ('-', '+', '*'),
           ('+', '*', '-'),
           ('+', '-', '*'),
           ('*', '+', '-'),
           ('*', '-', '+')]

    #우선 순위정하고
    result = []
    for mod in  mods:
        # 순서대로 계산을 돈다
        sig_tmp = sig.copy()
        num_tmp = num.copy()
        for m in mod:
            idx = 0
            sig_new = []
            for i, next in enumerate(sig_tmp):
                # 연산을 해야된다면
                if m == next:
                    # 계산하고 제거하고 삽입
                    if m == '+':
                        new_num = num_tmp.pop(idx) + num_tmp.pop(idx)
                    elif m == '-':
                        new_num = num_tmp.pop(idx) - num_tmp.pop(idx)
                    else:
                        new_num = num_tmp.pop(idx) * num_tmp.pop(idx)

                    try:
                        num_tmp = num_tmp[:idx] + [new_num] + num_tmp[idx:]
                    except:
                        num_tmp = num_tmp[:idx] + [new_num]

                    # 연산 시행한 경우 idx 앞으로 이동
                    idx -= 1

                else:
                    sig_new.append(next)
                sig_tmp = sig_new
                idx +=1

        result.append(abs(num_tmp.pop()))

    answer = max(result)

    return answer

'''
1. 배열 두개를 이용하는 발상
2. 직관적으로 짜는 습관 
3. pop 때문에 배열길이가 변하는 경우 idx 직접 조정하기
'''