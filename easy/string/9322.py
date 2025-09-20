"""
문제: 철벽 보안 알고리즘
유형: 문자열/집합과 맵
난이도: S

시간복잡도: O(t x n^2)
공간복잡도: O(n)

아이디어:
1. 제 1공개키 -> 제 2공개키 변환 규칙
2. 암호문에 역규칙을 적용

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
t =  int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

# [핵심 로직]
    f = list(sys.stdin.readline().split())
    s = list(sys.stdin.readline().split())
    c = list(sys.stdin.readline().split())

    li = [s.index(i) for i in f]
    ans = [c[j] for j in li]

# [결과 출력]
    print(*ans)
