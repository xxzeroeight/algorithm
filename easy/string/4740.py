"""
문장이 주어지면, 거꾸로 바뀐 문장을 출력한다.

예제 1:
입력:
AMBULANCE
Evian
madam, i'm adam
***
출력:
ECNALUBMA
naivE
mada m'i ,madam

제약 조건:
각 문장은 최소 1글자에서 최대 80글자로 이루어져 있다.
문장은 알파벳, 숫자, 공백, 구두점으로 구성된다.
"""

import sys

# [입력 처리]
while 1:
    s = sys.stdin.readline().rstrip("\n")

# [핵심 로직]
    if s == "***":
        break

# [결과 출력]
    print(s[::-1])
