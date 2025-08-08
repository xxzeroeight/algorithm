"""
문자열이 주어지면, "JOI"와 "IOI"의 갯수를 센다.

예제 1:
입력: JOIJOI
출력:
2
0

예제 2:
입력: JOIOIOIOI
출력:
1
3

예제 3:
입력: JOIOIJOINXNXJIOIOIOJ
출력:
2
3
"""

import sys

# [입력 처리]
s = sys.stdin.readline()

# [핵심 로직]
i, j = 0, 0
for k in range(len(s)-2):
    if s[k:k+3] == "JOI":
        j += 1

    if s[k:k+3] == "IOI":
        i += 1

# [결과 출력]
print(j)
print(i)
