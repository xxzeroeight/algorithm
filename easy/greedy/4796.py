"""
V일 휴가가 주어지면, P일을 주기로 L일만큼 캠핑장을 이용한다.
P일 주기가 시작되면 다시 L일까지 사용할 수 있다.

예제 1:
입력:
5 8 20
5 8 17
0 0 0
출력:
Case 1: 14
Case 2: 11

제약 조건:
1 < L < P < V
"""

import sys

# [입력 처리]
i = 1
while 1:
    l, p, v = map(int, sys.stdin.readline().split())

# [핵심 로직]
    if l == p == v == 0:
        break

    print(f"Case {i}: {l*(v//p) + min(v%p, l)}")

    i += 1

# [결과 출력]

