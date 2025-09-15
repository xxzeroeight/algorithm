"""
문제: 폴리오미노
유형: 그리디/문자열
난이도: S

시간복잡도: O(n)
공간복잡도: O(n)

아이디어:
1. "XXXX", "XX"를 "AAAA", "BB"로 대체한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
s = sys.stdin.readline().rstrip()

# [핵심 로직]
s = s.replace("XXXX", "AAAA")
s = s.replace("XX", "BB")

# [결과 출력]
if "X" in s: print(-1)
else: print(s)
