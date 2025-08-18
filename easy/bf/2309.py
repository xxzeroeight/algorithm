"""
아홉 개의 정수가 주어지면, 합이 100인 정수 일곱 개를 찾는다.

예제 1:
입력:
20
7
23
19
10
15
25
8
13
출력:
7
8
10
13
19
20
23

제약 조건:
주어지는 키는 100을 넘지 않는 자연수이다.
"""

import sys

# [입력 처리]
h = [int(sys.stdin.readline().rstrip()) for _ in range(9)]

# [핵심 로직]
for i in range(len(h)-1):
    for j in range(i+1, len(h)):
        if sum(h) - (h[i] + h[j]) == 100:
            h.pop(j)
            h.pop(i)
            break

h.sort()

# [결과 출력]
print(*h, sep="\n")
