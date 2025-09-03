"""


예제 1:
입력:
출력:

제약 조건:

"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    li = [list(map(int, sys.stdin.readline().split()))[1:] for _ in range(n)]
    cnt = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
    ans = 0

# [결과 출력]
    print(ans)

# 2025-09-03, 시도: 2