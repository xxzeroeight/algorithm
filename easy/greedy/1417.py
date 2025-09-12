"""
문제: 국회의원 선거
유형: 그리디
난이도: S

시간복잡도: O(k x n)
공간복잡도: O(n)

아이디어:
1. 다솜이의 표가 후보 중 가장 많을 때까지 현재 표가 가장 많은 사람을 반복 매수한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())
dasom = int(sys.stdin.readline())
candidates = [int(sys.stdin.readline()) for _ in range(n-1)]

# [핵심 로직]
cnt = 0
while 1:
    if dasom > max(candidates):
        break

    p = candidates.index(max(candidates))
    candidates[p] -= 1
    dasom += 1
    cnt += 1

# [결과 출력]
print(cnt)
