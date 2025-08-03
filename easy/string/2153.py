"""
# 문제 정보

문제: [소수 단어]
출처: [백준 2153]
난이도: [B2]
분류: [문자열]
"""

"""
# 메모

아이디어
 - 아스키 코드로 변환된 문자들의 합이 소수인지 판별
주의 사항
 - "A"-"Z": 65~90
 - "a"-"z": 97~122
개선점
"""

import math
import sys

# [입력 처리]
words = sys.stdin.readline().rstrip()

# [핵심 로직]
def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

res = 0
for word in words:
    if 65 <= ord(word) <= 90:
        res += ord(word) - 38
    else:
        res += ord(word) - 96

# [결과 출력]
print("It is a prime word." if is_prime(res) else "It is not a prime word.")
