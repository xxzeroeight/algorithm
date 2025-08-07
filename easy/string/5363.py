"""
어떤 문장이 주어졌을 때, 요다의 말로 바꾼다.
요다는 모든 문장에서 가장 앞 단어 두 개를 제일 마지막에 말한다.

예제 1:
입력:
4
I will go now to find the Wookiee
Solo found the death star near planet Kessel
I'll fight Darth Maul here and now
Vader will find Luke before he can escape
출력:
go now to find the Wookiee I will
the death star near planet Kessel Solo found
Darth Maul here and now I'll fight
find Luke before he can escape Vader will

제약 조건:
문장의 길이는 100글자 이내이다. 단어의 개수는 3개 이상이다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

for _ in range(n):
    sentence = list(sys.stdin.readline().split())

# [핵심 로직]
    res = sentence[2:] + sentence[:2]

# [결과 출력]
    print(" ".join(res))
