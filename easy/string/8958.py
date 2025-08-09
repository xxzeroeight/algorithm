"""
"O"와 "X"로 이루어진 문자열이 주어지면, 연속된 "O"의 개수의 합을 구한다.

예제 1:
입력:
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
출력:
10
9
7
55
30

제약 조건:
길이가 0보다 크고 80보다 작은 문자열이 주어진다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

# [핵심 로직]
for _ in range(t):
    s = sys.stdin.readline().rstrip()

    res, cnt = 0, 0
    for w in s:
        if w == "O":
            cnt += 1
        else:
            cnt = 0

        res += cnt

# [결과 출력]
    print(res)
