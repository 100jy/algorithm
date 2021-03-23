from collections import deque


def solution(play_time, adv_time, logs):

    def get_idx(time):
        h = int(time[:2])
        m = int(time[3:5])
        s = int(time[-2:])
        return (60**2 * h) + (60 * m) + (s)

    max_time = get_idx(play_time)
    total_sum = [0 for _ in range(max_time + 1)]

    # 구간별 cnt
    for time in logs:
        start = get_idx(time[:8])
        end = get_idx(time[9:])
        for i in range(start, end+1):
            total_sum[i] += 1

    # 윈도우 이동하면서
    end_point = get_idx(adv_time)
    start_point = 1

    window = deque(total_sum[1:(end_point+1)])
    total_sum = deque(total_sum[(end_point+1):])
    sum_time = sum(window)

    answer = start_point
    max_sum = sum_time

    # 맥시멈 구간 찾는다?
    while total_sum:
        start_point += 1
        left = window.popleft()
        right = total_sum.popleft()
        window.append(right)
        sum_time = sum_time - left + right
        if sum_time > max_sum:
            answer = start_point
            max_sum = sum_time

    def inverse(time):
        h = time // (60**2)
        m = (time - h*(60**2)) // 60
        s = (time - h*(60**2) - m*(60))

        def zeros(h):
            if h < 10:
                h = '0' + str(h)
            else:
                h = str(h)
            return h

        return '{}:{}:{}'.format(zeros(h), zeros(m), zeros(s))

    return inverse(answer)