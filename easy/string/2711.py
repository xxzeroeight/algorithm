"""
오타를 낸 문장과 위치가 주어졌을 때, 오타를 지운 문장을 출력한다.

예제 1:
입력:
4
4 MISSPELL
1 PROGRAMMING
7 CONTEST
3 BALLOON
출력:
MISPELL
ROGRAMMING
CONTES
BALOON

제약 조건:
테스트 케이스의 개수 T(1<=T<=1,000)
문자열의 길이는 80을 넘지 않고, 대문자로만 이루어져 있다. 오타를 낸 위치는 문자열 길이보다 작거나 같다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    p, s = sys.stdin.readline().split()

# [핵심 로직]


# [결과 출력]
    print(s[:int(p)-1] + s[int(p):])
