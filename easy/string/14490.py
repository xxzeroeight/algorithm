"""
두 정수가 주어졌을 때, 두 수를 최대한 약분한다.

예제 1:
입력: 100:10
출력: 10:1

예제 2:
입력: 18:24
출력: 3:4

제약 조건:
1 ≤ n, m ≤ 100,000,000

풀이:
1. n, m의 최대공약수로 각각 나눈다.
"""

import math
import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split(":"))

# [핵심 로직]
p = math.gcd(n, m)

# [결과 출력]
print(f"{n//p}:{m//p}")
