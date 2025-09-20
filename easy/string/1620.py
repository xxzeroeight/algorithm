"""
문제: 나는야 포켓몬 마스터 이다솜
유형: 집합과 맵
난이도: S

시간복잡도: O(n + m)
공간복잡도: O(n x L)

아이디어:
1. 해시를 이용하여 키-값을 각각 구한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())

dict = {}
for i in range(1, n+1):
    s = sys.stdin.readline().rstrip()

    dict[s] = i
    dict[i] = s

# [핵심 로직]
for _ in range(m):
    q = sys.stdin.readline().rstrip()

    if q.isdigit():
        print(dict[int(q)])
    else:
        print(dict[q])

# [결과 출력]

