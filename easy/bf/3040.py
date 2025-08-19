"""
아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾는다.

예제 1:
입력:
7
8
10
13
15
19
20
23
25
출력:
7
8
10
13
19
20
23

예제 2:
입력:
8
6
5
1
37
30
28
22
36
출력:
8
6
5
1
30
28
22

제약 조건:
총 아홉개 줄에 1보다 크거나 같고 99보다 작거나 같은 자연수가 주어진다.
"""

import sys

# [입력 처리]
h = [int(sys.stdin.readline().rstrip()) for _ in range(9)]

# [핵심 로직]
for i in range(len(h)-1):
    for j in range(i+1, len(h)):
        if sum(h) - (h[i]+h[j]) == 100:
            h.pop(j)
            h.pop(i)
            break

h.sort()

# [결과 출력]
print(*h, sep="\n")
