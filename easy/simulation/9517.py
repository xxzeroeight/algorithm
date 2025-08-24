"""


예제 1:
입력:
1
5
20 T
50 T
80 T
50 T
30 T
출력:
5

예제 2:
입력:
3
5
100 T
100 N
100 T
100 T
100 N
출력:
4

예제 3:
입력:
5
6
70 T
50 P
30 N
50 T
30 P
80 T
출력:
7

제약 조건:
1 ≤ K ≤ 8
1 ≤ N ≤ 100
1 ≤ T ≤ 100
"""

import sys

# [입력 처리]
k = int(sys.stdin.readline())
n = int(sys.stdin.readline())

l = 0
people = [i for i in range(1, 9)]
for i in range(n):
    t, z = sys.stdin.readline().split()

# [핵심 로직]
    l += int(t)

    if l > 210:
        break

    if z == "T":
        k = (k+1) % 8
    else:
        continue

# [결과 출력]
    print(people[k-1])

# 2025-08-24, 시도: 2