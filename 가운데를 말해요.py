# 이때까지의 입력중에 중간값 찾기
# 정렬문제
# 짝수개일 경우 더 작은 값


######################################################
# 힙정렬
# 힙의 특성을 이용한 정렬
# O(nlogn)
# 제자리 정렬
# 완전 이진트리에 가까운 형태
# 이진트리는 각노드의 자식수가 2이하인 트리
# 완전 이진 트리는 root 노드부터 Leaf 노드까지 빠짐없이
# 채워져있는 트리

# 최대힙
# 부모노드의 값이 자식노드의 값보다 항상 크거나 같다
# 하위트리 구조에서 root 노드가 가장 큰값을 가짐(최대값보장)

# 최소힙
# 부모노드의 값이 자식노드의 값보다 항상 작거나 같다
# 하위트리 구조에서 root 노드가 가장 작은 값을 가짐(최솟값 보장)
# 루트노드를 배열의 가장 첫값에 저장
# 각 노드들을 레벨별로 저장

#   16
#  14 10
# 8 7 9 3
# 입력에 대해서
# 16 14 10 8 7 9 3 순서로 배열 저장

# 힙의 검색
# parent(i) = arr[i/2]
# Left(i) = arr[2*i]
# Right(i) = arr[2*i + 1]
# 트리의 높이 = O(logn)

# max heapify
# root부터 규칙을 만족하는지 확인(flow down)
# 규칙어길시 하위노드값중 큰값을 부모로 올리고 부모를 흘려내린다.
# 수행시간은 O(logn)
######################################################

######################################################
# 문제조건 N : 정수의 개수
# 최대힙, 최소힙을 이용한 중앙값 구하기 알고리즘
# 1. 최대힙의 크기는 최소힙의 크기와 같거나 하나가 더크다(홀,짝)
# 2. 최대힙의 최대 원소는 최소힙의 최소 원소보다 작거나 같다
# 3. 조건이 맞지 않다면 최소힙과 최대힙의 꼭대기를 교환
# 조건하에서 최대힙의 top값이 항상 중간값
# 참고
# https://www.crocus.co.kr/625
######################################################

# heapq 모듈의 메써드이용해서 배열을 heapify 할 수 있다.
# 파이썬은 기본적으로 minheap
import heapq
import sys

#메인 함수
def get_median(integer, max_heap, min_heap):
    # 최대힙이나 최소힙에 삽입
    if len(max_heap) == len(min_heap):
        # 최대힙(우선순위, 값)
        heapq.heappush(max_heap, (-integer, integer))
    else:
        heapq.heappush(min_heap, integer)

    # 비교
    if  min_heap == []:
        return max_heap[0][1] , max_heap, min_heap

    if max_heap[0][1] > min_heap[0]:
        # 스왑
        maxtop = heapq.heappop(max_heap)[1]
        mintop = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-mintop, mintop))
        heapq.heappush(min_heap, maxtop)
    # 최대힙의 top값을 return
    return max_heap[0][1] , max_heap, min_heap


#입출력
if __name__ == '__main__':
    # 입력처리
    N = int(sys.stdin.readline())
    # 초기화
    max_heap = []
    min_heap = []

    for i in range(N):
        integer = int(sys.stdin.readline())
        median, max_heap, min_heap =  get_median(integer, max_heap, min_heap)
        print(median)



##### review ###############################################
# input() 함수 매우 느림 -> sys.stdin.readline() 사용할 것
# heaq 개념, heeaq 모듈 복습
# 중앙값 구하기 알고리즘 이해
############################################################


