"""
0과 1로 이루어진 문자열이 주어진다. 문자열의 양 끝에서 수를 하나씩 고르고, 두 수를 비교한다.
마지막으로 고르는 두 숫자로 결정을 내린다.

예제 1:
입력:
3
00100010
01010101
100001
출력:
Do-it
Do-it-Not
Do-it

제약 조건:
1 ≤ N ≤ 1000
문자열의 길이는 항상 짝수이고, 1000보다 작다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline()

# [핵심 로직]


# [결과 출력]
    print("Do-it" if s[len(s)//2-1] == s[len(s)//2] else "Do-it-Not")
