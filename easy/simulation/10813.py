"""
공을 바꿀 바구니 2개를 선택하고, 안에 들어있는 공을 서로 교환한다.

예제 1:
입력:
5 4
1 2
3 4
1 4
2 2
출력:
3 1 4 2 5

제약 조건:
1 ≤ N ≤ 100
1 ≤ M ≤ 100
1 ≤ i ≤ j ≤ N
"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())

check = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

# [핵심 로직]
    check[i-1], check[j-1] = check[j-1], check[i-1]

# [결과 출력]
print(*check)
