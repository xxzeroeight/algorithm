"""
문자열이 주어지면, 모두 소문자로 변환한다.

예제 1:
입력:
3
WatanabE
ITO
YamaMoto
출력:
watanabe
ito
yamamoto

예제 2:
입력:
4
SUZUKI
tanaka
tAkAhAshi
SuZuKi
출력:
suzuki
tanaka
takahashi
suzuki

제약 조건:
N(1 ≤ N ≤ 100)
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().rstrip()

# [핵심 로직]


# [결과 출력]
    print(s.lower())
