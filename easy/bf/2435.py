"""
연속적인 K만큼의 합이 최대가 되는 값을 출력한다.

예제 1:
입력:
10 2
3 -2 -4 -9 0 3 7 13 8 -3
출력:
21

제약 조건:
2<=N<=100
"""

import sys

# [입력 처리]
n, k = map(int, sys.stdin.readline().split())
tem = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
mv = -100000
for i in range(n-k+1):
    mv = max(mv, sum(tem[i:i+k]))

# [결과 출력]
print(mv)
