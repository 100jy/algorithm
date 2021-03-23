#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'taxiDriver' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY pickup
#  2. LONG_INTEGER_ARRAY drop
#  3. INTEGER_ARRAY tip
#
from collections import deque
def taxiDriver(pickup, drop, tip):
    # Write your code here
    def BFS(q, pickup=pickup, drop=drop, tip=tip):
        end_point = pickup[-1]
        max_m = 0
        while q:
            p, d, m, idx = q.popleft()
            for agree in (0,1):
                # d가 max(p) 넘으면 종료
                if d > end_point:
                    if m > max_m:
                        max_m = m
                    continue
                #태울 수 있는 손님 태우기
                new_p = pickup[idx]
                new_d = drop[idx]
                while new_p < d:
                    idx+=1
                    new_p = pickup[idx]
                    new_d = drop[idx]
                if agree:
                    m += new_d - new_p + tip[idx]
                    q.append([new_p, new_d, m, idx])
                    # 건너뛰기
                else:
                    q.append([p, d, m, idx+1])
        return max_m


    q = deque([[0,0,0,0]])
    max_m = BFS(q)
    return max_m



taxiDriver([])