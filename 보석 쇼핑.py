# 계수정렬 문제였넼ㅋㅋ
# 전체 길이가 100,000 이라서 가능???

# map이용
# l, r pointer 이용
# map에 전체 보석 있다면 더 좋은 답인지 체크 후 l증가 (범위 줄이기)
# 전체 보석이 없다면 r을 증가(범위 늘리기)
# 종료조건은 어떻게????
from collections import defaultdict
def solution(gems):
    answer = [0, 1e+5]
    dict = defaultdict(int)
    for gem in gems:
        dict[gem] += 1
    gem_total = len(dict)

    # 포인터 초기화
    l_pointer,r_pointer = 1, 1
    bag_dict = defaultdict(int)
    bag_dict[gems[0]] += 1
    #진열대의 범위를 초과하면 종료
    while 0<l_pointer<=len(gems) and 0<r_pointer<=len(gems):

        # 보석이 충분하면 기록 측정 및 길이 줄여주기
        if len(bag_dict) == gem_total:
            # 최고기로기록이면 갱신
            if (r_pointer-l_pointer) < (answer[1] - answer[0]):
                answer = [l_pointer, r_pointer]
            # bag에 보석하나 덜기
            bag_dict[gems[l_pointer-1]] -= 1
            # 빈도가 0이면 없애주기
            if bag_dict[gems[l_pointer-1]] == 0:
                del bag_dict[gems[l_pointer-1]]
            # 포인터 이동
            l_pointer +=1
            if r_pointer >len(gems):
                break
        # 보석이 부족하면 길이추가
        elif len(bag_dict) < gem_total:
            # 포인터 이동하고
            r_pointer +=1
            if r_pointer >len(gems):
                break
            # bag에 보석하나 추가
            bag_dict[gems[r_pointer-1]] += 1

    return answer

solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"])