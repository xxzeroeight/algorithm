"""
정수 N과 M이 주어졌을 때, N부터 M까지의 0의 개수를 센다.

예제 1:
입력:
3
0 10
33 1005
1 4
출력:
2
199
0

제약 조건:
1 ≤ T ≤ 20
0 ≤ N ≤ M ≤ 1,000,000
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

# [핵심 로직]
    cnt = 0
    for i in range(n, m+1):
        cnt += str(i).count("0")

# [결과 출력]
    print(cnt)
