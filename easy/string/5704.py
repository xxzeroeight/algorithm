"""
문자열이 주어지면, 팬그램(알파벳의 모든 글자를 사용하여 만든 문장)인지 판단한다.

예제 1:
입력:
jackdawf loves my big quartz sphinx
abcdefghijklmnopqrstuvwxyz
hello world
*
출력:
Y
Y
N

제약 조건:
각 테스트 케이스는 많아야 200글자로 이루어져 있는 문장이다.
단어는 공백 하나로 구분되어 있다.
"""

import sys

# [입력 처리]
while 1:
    s = list(sys.stdin.readline().rstrip())

# [핵심 로직]
    if s[0] == "*":
        break

    check = [0] * 26
    for w in s:
        if w == " ":
            continue

        check[ord(w) - 97] = 1

# [결과 출력]
    print("Y" if sum(check) == 26 else "N")
