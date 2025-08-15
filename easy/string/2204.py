"""
문자열이 주어지면, 대소문자를 구분하지 않고 사전순으로 오름차순 정렬한다.

예제 1:
입력:
3
Cat
fat
bAt
4
call
ball
All
Hall
0
출력:
bAt
All

제약 조건:
2 ≤ n ≤ 1000
"""

import sys

# [입력 처리]
while 1:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    li = sorted([sys.stdin.readline().rstrip() for _ in range(n)], key=lambda x: x.lower())

# [핵심 로직]


# [결과 출력]
    print(li[0])
