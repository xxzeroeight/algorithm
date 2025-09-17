"""
문제: 짐 챙기는 숌
유형: 그리디/시뮬레이션
난이도: S

시간복잡도: O(n)
공간복잡도: O(n)

아이디어:
1. 책을 순서대로 현재 상자에 넣을 수 있으면 넣고, 넣을 수 없으면 새로운 상자를 사용한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
if n == 0:
    print(0)
    quit()

cnt, tmp = 1, 0
for book in books:
    if tmp+book > m:
        cnt += 1
        tmp = book
    else:
        tmp += book

# [결과 출력]
print(cnt)
