"""
문자열이 주어지면, 문자열의 첫 글자와 마지막 글자를 출력한다.

예제 1:
입력:
3
ACDKJFOWIEGHE
O
AB
출력:
AE
OO
AB

제약 조건:
테스트 케이스의 개수 T(1 ≤ T ≤ 10)
문자열의 길이는 1000보다 작다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().rstrip()

# [핵심 로직]


# [결과 출력]
    print(s[0] + s[-1])
