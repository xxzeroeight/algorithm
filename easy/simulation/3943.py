"""
헤일수톤 수열에서 가장 큰 값을 출력한다.

예제 1:
입력:
4
1
3
9999
100000
출력:
1
16
101248
100000

제약 조건:
1 ≤ T ≤ 100,000
1 ≤ n ≤ 100,000
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

# [핵심 로직]
    mv = n
    while 1:
        if n == 1:
            break

        if n % 2 == 0:
            n //= 2
        else:
            n = (n*3)+1

        mv = max(mv, n)

# [결과 출력]
    print(mv)
