"""
N개의 문제(쉬움, 어려움)가 주어졌을 때, 문제를 최대한 풀어 얻을 수 있는 최대값을 출력한다.

예제 1:
입력:
4 8 4
1 8
4 5
6 20
9 12
출력:
380

예제 2:
입력:
8 7 5
1 3
2 5
3 5
4 8
5 8
6 9
6 7
7 10
출력:
660

예제 3:
입력:
8 9 5
1 8
3 10
4 5
5 20
7 12
8 15
9 50
14 14
출력:
580

제약 조건:
1 ≤ N ≤ 100
1 ≤ L ≤ 50
1 ≤ sub1 ≤ sub2 ≤ 50

서브태스크 1:
K = N

서브태스크 2:
0 ≤ K ≤ N
"""

import sys

# [입력 처리]
n, l, k = map(int, sys.stdin.readline().split())

p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# [핵심 로직]
p = sorted(p, key=lambda x: x[1])

score = 0
for i in range(k):
    if p[i][1] <= l:
        score += 140
    elif p[i][0] <= l:
        score += 100

# [결과 출력]
print(score)
