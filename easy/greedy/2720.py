"""
거스름돈의 액수가 주어지면, 동전의 개수를 최소화하여 거슬러준다.

예제 1:
입력:
3
124
25
194
출력:
4 2 0 4
1 0 0 0
7 1 1 4

제약 조건:
1<=C<=500
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    c = int(sys.stdin.readline())

# [핵심 로직]
    coins = [25, 10, 5, 1]
    ans = [0, 0, 0, 0]

    for i in range(4):
        ans[i] = c // coins[i]
        c %= coins[i]

# [결과 출력]
    print(*ans)
