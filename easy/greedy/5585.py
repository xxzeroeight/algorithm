"""
지불한 돈이 정수로 주어진다.
1000원을 내고 받을 잔돈의 개수를 센다.

예제 1:
입력: 380
출력: 4

예제 2:
입력: 1
출력: 15

제약 조건:
1 <= m < 1000
"""

import sys

# [입력 처리]
m = int(sys.stdin.readline())

# [핵심 로직]
coins = [500, 100, 50, 10, 5, 1]
ans = [0, 0, 0, 0, 0, 0]

balance = 1000 - m
for i in range(6):
    ans[i] = balance // coins[i]
    balance %= coins[i]

# [결과 출력]
print(sum(ans))
