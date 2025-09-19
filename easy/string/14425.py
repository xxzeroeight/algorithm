"""
문제: 문자열 집합
유형: 문자열/집합과 맵
난이도: S

시간복잡도: O(n + m)
공간복잡도: O(n)

아이디어:
1. 주어지는 문자열이 집합 S에 포함되어 있는지 확인하는 문제이다. (set())

주의할 점/예외 케이스:
1. 리스트로 풀면 시간초과이다.
"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())

# [핵심 로직]
tmp = set()
for _ in range(n):
    tmp.add(sys.stdin.readline().rstrip())

cnt = 0
for _ in range(m):
    s = sys.stdin.readline().rstrip()

    if s in tmp:
        cnt += 1

# [결과 출력]
print(cnt)
