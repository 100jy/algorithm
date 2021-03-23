def solution(lines):
    answer = 0
    # 1초간 처리하는 최대 프로세스

    import heapq

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

    # 끝시간 힙에 넣고
    # 시작시간 보다 1초 이상 작은 것들 다뺴주고 카운트
    heap = []
    for log in lines:
        end_time, pt = get_abs_time(log)
        start_time = end_time - pt + 1

        heap.append()

        while start_time - heap[0] > 1:
            heapq.heappop(heap)

        if len(heap)




    return answer