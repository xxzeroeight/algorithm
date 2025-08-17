"""
문자열이 주어지면, 글자들을 빈틈없이 세로로 나열한다.

예제 1:
입력:
ABCDE
abcde
01234
FGHIJ
fghij
출력:
Aa0FfBb1GgCc2HhDd3IiEe4Jj

예제 2:
입력:
AABCDD
afzz
09121
a8EWg6
P5h3kx
출력:
Aa0aPAf985Bz1EhCz2W3D1gkD6x
"""

import sys

# [입력 처리]
s = [sys.stdin.readline().rstrip() for _ in range(5)]

# [핵심 로직]
max_len = max(len(w) for w in s)

li = [w+("*" * (max_len - len(w))) for w in s]

# [결과 출력]
res = [li[j][i] for i in range(max_len) for j in range(5)]

print("".join(res).replace("*", ""))
