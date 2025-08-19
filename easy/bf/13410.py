"""
거꾸로된 N단 구구단중 가장 큰 값을 찾는다.

예제 1:
입력: 8 9
출력: 84

제약 조건:
N <= k <= 1,000
"""

import sys

# [입력 처리]
n, k = map(int, sys.stdin.readline().split())

# [핵심 로직]
ans = [int(str(n*i)[::-1]) for i in range(1, k+1)]

# [결과 출력]
print(max(ans))
