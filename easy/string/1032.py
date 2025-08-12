"""
문자열들이 주어지면, 파일 검색 패턴을 작성한다.

예제 1:
입력:
3
config.sys
config.inf
configures
출력:
config????

예제 2:
입력:
2
contest.txt
context.txt
출력:
conte?t.txt

예제 3:
입력:
3
c.user.mike.programs
c.user.nike.programs
c.user.rice.programs
출력:
c.user.?i?e.programs

제약 조건:
N은 50보다 작거나 같은 자연수이고 파일 이름의 길이는 모두 같고 길이는 최대 50이다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

origin = list(sys.stdin.readline().rstrip())
for _ in range(n-1):
    s = list(sys.stdin.readline().rstrip())

    for i in range(len(origin)):
        if origin[i] != s[i]:
            origin[i] = "?"

# [핵심 로직]


# [결과 출력]
print("".join(origin))