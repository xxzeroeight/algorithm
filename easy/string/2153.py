"""
알파벳 하나가 주어지며 스펠링을 숫자로 변환하여 그 합을 구한다.
합이 소수인지 아닌지 판단한다.

예제 1:
입력: UFRN
출력: It is a prime word.

예제 2:
입력: contest
출력: It is not a prime word.

제약 조건:
단어의 길이는 20자 이하이다.
주어지는 단어는 알파벳 소문자와 대문자만으로 이루어져 있다.
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
