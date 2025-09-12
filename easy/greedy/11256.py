"""
문제: 사탕
유형: 그리디/정렬
난이도: S

시간복잡도: O(t x nlogn)
공간복잡도: O(n)

아이디어:
1. 상자를 최소한으로 사용하기 위해서 크기가 큰 상자부터 사용한다.
2. 상자를 다 채울 필요는 없다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    j, n = map(int, sys.stdin.readline().split())

    li = []
    for _ in range(n):
        r, c = map(int, sys.stdin.readline().split())
        li.append(r*c)

    li.sort(reverse=True)

# [핵심 로직]
    cnt = 0
    for l in li:
        if j <= 0:
            break
        else:
            j -= l
            cnt += 1

# [결과 출력]
    print(cnt)
