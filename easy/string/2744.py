"""
알파벳으로 이루어진 문자열을 입력받아 소문자는 대문자로 대문자는 소문자로 변환한 후 출력한다.

예제 1:
입력: WrongAnswer
출력: wRONGaNSWER

제약 조건:
영어 소문자와 대문자로만 이루어진 단어가 주어진다.
단어의 길이는 최대 100이다.
"""

import sys

# [입력 처리]
sentence = sys.stdin.readline().rstrip()

# [핵심 로직]
res = ""
for word in sentence:
    if word.isupper():
        res += word.lower()
    else:
        res += word.upper()

# [결과 출력]
print(res)
