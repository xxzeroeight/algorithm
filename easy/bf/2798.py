"""
3장의 카드를 골라 M을 넘지 않으면서 최대한 가깝게 만든다.

예제 1:
입력:
5 21
5 6 7 8 9
출력:
21

예제 2:
입력:
10 500
93 181 245 214 315 36 185 138 216 295
출력:
497

제약 조건:
3 ≤ N ≤ 100
10 ≤ M ≤ 300,000
"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
mv = 0
for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            if cards[i] + cards[j] + cards[k] <= m:
                mv = max(mv, cards[i] + cards[j] + cards[k])

# [결과 출력]
print(mv)
