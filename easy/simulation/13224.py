"""
주어지는 문자에 따라 공의 위치를 바꾼다.

예제 1:
입력: AB
출력: 3

예제 2:
입력: CBABCACCC
출력: 1
"""

import sys

# [입력 처리]
s = sys.stdin.readline().rstrip()

# [핵심 로직]
cups = [1, 0, 0]
for w in s:
    if w == "A":
        cups[0], cups[1] = cups[1], cups[0]
    elif w == "B":
        cups[1], cups[2] = cups[2], cups[1]
    else:
        cups[0], cups[2] = cups[2], cups[0]

# [결과 출력]
print(cups.index(1)+1)
