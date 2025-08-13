"""
두 문자열이 애너그램(알파벳의 순서를 바꾸어도 같은 문자열)인지 판단한다.

예제 1:
입력:
3
blather reblath
maryland landam
bizarre brazier
출력:
blather & reblath are anagrams.
maryland & landam are NOT anagrams.
bizarre & brazier are anagrams.

제약 조건:
테스트 케이스의 개수(<100)
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    a, b = sys.stdin.readline().split()

# [핵심 로직]


# [결과 출력]
    print(f"{a} & {b} are anagrams." if sorted(a) == sorted(b) else f"{a} & {b} are NOT anagrams.")
