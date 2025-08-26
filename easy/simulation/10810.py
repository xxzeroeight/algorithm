"""
공을 넣을 바구니 범위가 주어지면, 해당 바구니에 k를 넣는다.

예제 1:
입력:
5 4
1 2 3
3 4 4
1 4 1
2 2 2
출력:
1 2 1 1 0

제약 조건:
1 ≤ N ≤ 100
1 ≤ M ≤ 100
1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N
"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())

check = [0] * n
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())

# [핵심 로직]
    check[i-1:j] = [k] * (j-i+1)

# [결과 출력]
print(*check)
