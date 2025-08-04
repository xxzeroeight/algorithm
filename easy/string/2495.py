"""
여덟 자리의 양의 정수가 주어진다.
같은 숫자가 연속해서 나오는 구간 중 가장 긴 것의 길이를 출력한다. 없으면 1을 출력한다.

예제 1:
입력:
12345123
17772345
22233331
출력:
1
3
4
"""

import sys

# [입력 처리]
for _ in range(3):
    nums = sys.stdin.readline().rstrip()

# [핵심 로직]
    mv, cnt = 1, 1
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            cnt += 1
            mv = max(mv, cnt)
        else:
            cnt = 1

# [결과 출력]
    print(mv)
