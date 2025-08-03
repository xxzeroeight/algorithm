"""
2진수를 8진수로 변환한다.

예제 1:
입력: 11001100
출력: 314

제약 조건:
주어지는 수의 길이는 1,000,000을 넘지 않는다.
"""

import sys

# [입력 처리]
bi = sys.stdin.readline().rstrip()

# [핵심 로직]
de = int(bi, 2)
result = oct(de)

# [결과 출력]
print(result[2:])
