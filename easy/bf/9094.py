"""
정수 n과 m이 주어졌을 때, 문제의 조건을 만족하도록 한다.

예제 1:
입력:
3
10 1
20 3
30 4
출력:
2
4
5

제약 조건:
두 수는 0보다 크고, 100보다 작거나 같다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

# [핵심 로직]
    cnt = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            if (i*i + j*j + m) % (i*j) == 0:
                cnt += 1

# [결과 출력]
    print(cnt)
