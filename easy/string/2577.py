"""
세 개의 자연수 A, B, C가 주어지며, A*B*C를 계산한 결과에 0~9까지의 각각의 숫자가 몇 번 쓰였는지 센다.

예제 1:
입력:
150
266
427
출력:
3
1
0
2
0
0
0
2
0
0

제약 조건:
A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
"""

import sys

# [입력 처리]
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

# [핵심 로직]
check = [0] * 10
for i in str(a*b*c):
    check[int(i)] += 1

# [결과 출력]
print(*check, sep="\n")
