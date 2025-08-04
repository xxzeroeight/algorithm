"""
영어 문장과 알파벳 하나가 주어진다. 문장에서 알파벳이 몇 번 나타나는지 센다.

예제 1:
입력:
g Programming Contest
n New Zealand
x This is quite a simple problem.
#
출력:
g 2
n 2
x 0

제약 조건:
각 문장은 길이가 1에서 250이며 입력의 마지막은 #이다.
"""

import sys

# [입력 처리]
while 1:
    s = sys.stdin.readline().rstrip()

# [핵심 로직]
    if s == "#":
        break

    target = s[0]
    s = s[2:]

    cnt = 0
    for i in s:
        if i.lower() == target:
            cnt += 1

# [결과 출력]
    print(target, cnt)
