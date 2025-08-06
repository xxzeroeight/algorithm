"""
두 이진수가 주어졌을 때, 해밍 거리를 계산한다.

예제 1:
입력:
4
0
1
000
000
1111111100000000
0000000011111111
101
000
출력:
Hamming distance is 1.
Hamming distance is 0.
Hamming distance is 16.
Hamming distance is 2.

제약 조건:
두 이진수는 길이가 서로 같고, 100자리를 넘지 않는다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

# [핵심 로직]
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

# [결과 출력]
    print(f"Hamming distance is {cnt}.")
