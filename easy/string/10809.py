"""
문자열이 주어졌을 때,
알파벳이 문자열에 포함되어 있으면 처음 등장하는 위치를, 없으면 -1을 출력한다.

예제 1:
입력: baekjoon
출력: 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

제약 조건:
단어의 길이는 100을 넘지 않는다.
"""

import sys

# [입력 처리]
s = sys.stdin.readline().rstrip()

# [핵심 로직]
check = [-1] * 26
for w in s:
    check[ord(w)-97] = s.index(w)

# [결과 출력]
print(*check)
