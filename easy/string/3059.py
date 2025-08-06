"""
문자열이 주어졌을 때, 문자열에 등장하지 않는 알파벳의 아스키 코드 값의 합을 출력한다.

예제 1:
입력:
2
ABCDEFGHIJKLMNOPQRSTUVW
A
출력:
267
1950

제약 조건:
S는 알파벳 대문자로만 구성되어 있고, 최대 1000글자이다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    s = sys.stdin.readline().rstrip()

# [핵심 로직]
    check = [i for i in range(65, 91)]

    for w in s:
        check[ord(w)-65] = 0

# [결과 출력]
    print(sum(check))
