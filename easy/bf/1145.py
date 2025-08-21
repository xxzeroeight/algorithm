"""
자연수 다섯 개가 주어지면, 대부분의 배수(자연수 세 개의 최소공배수)를 출력한다.

예제 1:
입력: 30 42 70 35 90
출력: 210

예제 2:
입력: 1 2 3 4 5
출력: 4

예제 3:
입력: 30 45 23 26 56
출력: 1170

예제 4:
입력: 3 14 15 92 65
출력: 195
"""

import sys
from math import lcm

# [입력 처리]
nums = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
li = []
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            li.append(lcm(nums[i], nums[j], nums[k]))

# [결과 출력]
print(min(li))
