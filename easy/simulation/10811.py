"""
해당 범위에 들어있는 바구니의 순서를 역순으로 바꾼다.

예제 1:
입력:
5 4
1 2
3 4
1 4
2 2
출력:
3 4 1 2 5

제약 조건:
1 ≤ N ≤ 100
1 ≤ M ≤ 100
1 ≤ i ≤ j ≤ N
"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())

check = [k for k in range(1, n+1)]
for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())

# [핵심 로직]
    check[i-1:j] = check[i-1:j][::-1]

# [결과 출력]
print(*check)
