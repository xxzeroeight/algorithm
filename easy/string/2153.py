# ===== 문제 정보 =====
# 번호: 2153 | 문제: 소수 단어 | 난이도: Bronze 2
# 카테고리: 문자열

import math
import sys

# ===== 해결 전략 =====
# 아이디어: 아스키 코드로 변환된 문자들의 합이 소수인지 판별

# ===== 입력 처리 =====
words = sys.stdin.readline().rstrip()

# ===== 핵심 로직 =====
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

# ===== 결과 출력 =====
print("It is a prime word." if is_prime(res) else "It is not a prime word.")

# ===== 테스트 케이스 =====
# - 입력: UFRN
# - 출력: It is a prime word.

# - 입력: contest
# - 출력: It is not a prime word.

# ===== 메모 =====
# 주의사항
# - "A"-"Z": 65~90
# - "a"-"z": 97~122

# 실수한 부분
