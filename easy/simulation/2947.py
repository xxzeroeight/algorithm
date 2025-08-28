"""
숫자가 주어지면, 조건에 맞게 순서가 바뀔 때마다 출력한다.

예제 1:
입력:
2 1 5 3 4
출력:
1 2 5 3 4
1 2 3 5 4
1 2 3 4 5

예제 2:
입력:
2 3 4 5 1
출력:
2 3 4 1 5
2 3 1 4 5
2 1 3 4 5
1 2 3 4 5
"""

import sys

# [입력 처리]
nums = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
while 1:
    if nums == sorted(nums):
        break

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]

            print(*nums)

# [결과 출력]

