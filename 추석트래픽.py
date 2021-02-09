def solution(lines):
    answer = 0

    # 절대 시간 구해주기
    def get_abs_time(log):
        y = int(log[:4]) * 60*60*24*30.5*365

        m = int(log[5:7]) * 60*60*24*30.5
        d = int(log[8:10]) * 60*60*24

        h = int(log[11:13]) * 60*60
        M = int(log[14:16]) * 60
        try:
            s = float(log[16:16 + 7])
        except:
            s = float(log[17:16 + 7])

        pt = float(log[24:-1])

        return y + m + d + h + M + s, pt

    # 특정로그를 포함하는 1초구간중
    # 최대값은 종료시간부터 1초간의 구간을 세주면 된다.
    # 종료시간 순으로 정렬되어 있기때문

    for idx, log in enumerate(lines):
        end_time, pt = get_abs_time(log)
        window_end = end_time + 1 - 0.001
        # end_time부터 1초간의 구간에 들어오는 로그의 개수를 세준다.
        cnt = 1

        for next in lines[idx+1:]:
            next_end, pt = get_abs_time(next)
            start_time = next_end - pt + 0.001
            # start_time이 window_end내에 있다면
            if window_end >= start_time:
                cnt += 1
        if cnt > answer:
            answer = cnt

    return answer

#############################################################
# 먼저 문제 읽고
# 로직 생각해서
# 검증하고
# 계획해서 
# 코딩
# 디버깅
##############################################################