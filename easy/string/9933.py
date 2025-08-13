"""
비밀번호 목록에 비밀번호와 거꾸로 쓰여있는 비밀번호가 함께 있어야 한다.

예제 1:
입력:
4
las
god
psala
sal
출력: 3 a

예제 2:
입력:
4
kisik
ptq
tttrp
tulipan
출력: 5 s

제약 조건:
N (2 ≤ N ≤ 100)
단어는 알파벳 소문자로만 이루어져 있으며, 길이는 2보다 크고 14보다 작은 홀수이다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

li = [sys.stdin.readline().rstrip() for _ in range(n)]

# [핵심 로직]


# [결과 출력]
for l in li:
    if len(l) % 2 != 0 and l[::-1] in li:
        print(len(l), l[len(l)//2])
        break
