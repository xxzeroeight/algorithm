"""
팰린드롬(앞으로 읽으나 뒤로 읽으나 똑같은 문자열)인지 판단한다.

예제 1:
입력:
6
Nat tan
Palindrome
123454321
Dogs and Cats
**()()**
1 221
출력:
Yes
No
Yes
No
No
No
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

for _ in range(n):
    s = input().lower()

# [핵심 로직]


# [결과 출력]
    print("Yes" if s == s[::-1] else "No")
