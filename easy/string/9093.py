"""
문자열이 주어지면, 단어들을 모두 뒤집는다.

예제 1:
입력:
2
I am happy today
We want to win the first prize
출력:
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp

제약 조건:
단어의 길이는 최대 20, 문장의 길이는 최대 1000이다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    s = list(sys.stdin.readline().split())

# [핵심 로직]
    li = [w[::-1]  for w in s]

# [결과 출력]
    print(" ".join(li))
