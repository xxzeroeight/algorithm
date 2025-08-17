"""
자연수 N이 주어지면, N의 가장 작은 생성자를 구한다.

예제 1:
입력: 216
출력: 198

제약 조건:
1 ≤ N ≤ 1,000,000
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

# [핵심 로직]
for i in range(1, n):
    s = 0

    temp = i
    while temp > 0:
        s += temp % 10
        temp //= 10

    if n == i+s:
        print(i)
        break

# [결과 출력]
else:
    print(0)
