"""
문제: 뒤집기
유형: 그리디/문자열
난이도: S

시간복잡도: O(n)
공간복잡도: O(n)

아이디어:
1. "0"인 그룹의 개수와 "1"인 그룹의 개수 중 최소 횟수를 출력한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
s = sys.stdin.readline().rstrip()

# [핵심 로직]
g0 = s.split("1")
g1 = s.split("0")

cnt0 = len([i for i in g0 if i])
cnt1 = len([i for i in g1 if i])

# [결과 출력]
print(min(cnt0, cnt1))
