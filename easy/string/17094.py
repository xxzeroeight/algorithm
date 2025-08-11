"""
문자열의 "e"와 "2"중 등장횟수를 비교한다.

예제 1:
입력:
12
222eee222eee
출력: yee

예제 2:
입력:
3
22e
출력: 2

예제 3:
입력:
3
e2e
출력: e

제약 조건:
s의 길이는 1 이상 10^5 이하이다.
"""

import sys

# [입력 처리]
l = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

# [핵심 로직]


# [결과 출력]
print("2" if s.count("2") > s.count("e") else "e" if s.count("e") > s.count("2") else "yee")
