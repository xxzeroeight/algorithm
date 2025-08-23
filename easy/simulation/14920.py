"""
점화식에 맞게 반복하다가 처음으로 1이 되기까지의 횟수를 센다.

예제 1:
입력: 26
출력: 11

예제 2:
입력: 7
출력: 17

제약 조건:
1 ≤ C(1) ≤ 100000
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

# [핵심 로직]
cnt = 1
while 1:
    if n == 1:
        break

    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n+1

    cnt += 1

# [결과 출력]
print(cnt)
