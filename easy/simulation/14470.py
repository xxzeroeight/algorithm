"""
A도에서 B도까지 각 온도별 데우는 시간(C, D, E)을 이용하여 총 걸리는 시간을 출력한다.

예제 1:
입력:
-10
20
5
10
3
출력:
120

예제 2:
입력:
35
92
31
50
11
출력:
627

제약 조건:
A는 -100 이상 100 이하이며, 0이 아니다.
B는 1 이상 100 이하이며, A보다 크다.
C, D, E는 모두 1 이상 100 이하이다.
"""

import sys

# [입력 처리]
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())

# [핵심 로직]
s = 0
if a > 0:
    s += (b-a)*e
else:
    s += abs(a)*c + d + (b*e)

# [결과 출력]
print(s)
