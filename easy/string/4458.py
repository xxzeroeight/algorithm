"""
문장이 주어지면, 가장 첫 글자를 대문자로 바꾼다.

예제 1:
입력:
5
powdered Toast Man
skeletor
Electra Woman and Dyna Girl
she-Ra Princess of Power
darth Vader
출력:
Powdered Toast Man
Skeletor
Electra Woman and Dyna Girl
She-Ra Princess of Power
Darth Vader

제약 조건:
각 문장에 들어있는 글자의 수는 30을 넘지 않는다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    s = sys.stdin.readline().rstrip()

# [핵심 로직]


# [결과 출력]
    print(s[0].upper() + s[1:])
