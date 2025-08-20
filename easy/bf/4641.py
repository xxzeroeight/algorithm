"""
리스트 안에서 자신*2인 수를 찾는다.

예제 1:
입력:
1 4 3 2 9 7 18 22 0
2 4 8 10 0
7 5 11 13 1 3 0
-1
출력:
3
2
0
"""

import sys

# [입력 처리]
while 1:
    nums = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
    if nums[0] == -1:
        break

    cnt = 0
    for n in nums:
        if n*2 in nums:
            cnt += 1

# [결과 출력]
    print(cnt-1)
