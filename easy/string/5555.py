"""
찾고자하는 문자열이 주어졌을 때, 해당 문자열이 포함되어 있는 반지의 개수를 센다.

예제 1:
입력:
ABCD
3
ABCDXXXXXX
YYYYABCDXX
DCBAZZZZZZ
출력:
2

예제 2:
입력:
XYZ
1
ZAAAAAAAXY
출력:
1

예제 3:
입력:
PQR
3
PQRAAAAPQR
BBPQRBBBBB
CCCCCCCCCC
출력:
2

제약 조건:
1 ≦ N ≦ 100
1 ≦ i ≦ N

풀이:
1. 반지는 문자열의 시작과 끝이 연결되어 있다. (ZAAAAAAAXY -> ZAAAAAAAXYZ)
2. 반지에서 문자열을 찾는다.
"""

import sys

# [입력 처리]
find = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

# [핵심 로직]
cnt = 0
for _ in range(n):
    s = sys.stdin.readline().rstrip()

    ring = s + s[:len(find)-1]

    if find in ring:
        cnt += 1

# [결과 출력]
print(cnt)
