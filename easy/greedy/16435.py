"""
문제: 스네이크버드
유형: 그리디/정렬
난이도: S

시간복잡도: O(nlogn)
공간복잡도: O(n)

아이디어:
1. 과일을 왼쪽부터 순서대로 먹을 필요없다.
2. 조건에 만족하는 과일을 먹으면서 더 이상 먹지 못하면 멈춘다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
n, l = map(int, sys.stdin.readline().split())
h = sorted(list(map(int, sys.stdin.readline().split())))

# [핵심 로직]
for i in h:
    if l >= i:
        l += 1
    else:
        break

# [결과 출력]
print(l)
