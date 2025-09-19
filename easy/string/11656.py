"""
문제: 접미사 배열
유형: 문자열/배열
난이도: S

시간복잡도: O(n^2logn)
공간복잡도: O(n^2)

아이디어:
1. 모든 접미사를 구한 뒤 정렬한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
s = sys.stdin.readline().rstrip()

# [핵심 로직]
ans = [s[i:] for i in range(len(s))]

ans.sort()

# [결과 출력]
print(*ans, sep="\n")
