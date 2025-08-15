"""
문자열이 주어지면, 팰린드롬인지 판단한다.

예제 1:
입력: level
출력: 1

예제 2:
입력: baekjoon
출력: 0

제약 조건:
단어의 길이는 1보다 크거나 같고, 100보다 작거나 같다.
"""

import sys

# [입력 처리]
s = sys.stdin.readline().rstrip()

# [핵심 로직]


# [결과 출력]
print("1" if s == s[::-1] else "0")
