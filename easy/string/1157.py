"""
문자열이 주어졌을 때, 이 문자열에서 가장 많이 사용된 알파벳을 찾는다.

예제 1:
입력: Mississipi
출력: ?

예제 2:
입력: zZa
출력: Z

예제 3:
입력: z
출력: Z

예제 4:
입력: baaa
출력: A

제약 조건:
주어지는 단어의 길이는 1,000,000을 넘지 않는다.
"""

import sys

# [입력 처리]
s = sys.stdin.readline().rstrip().lower()

# [핵심 로직]
check = [0] * 26
for w in s:
    check[ord(w)-97] += 1

# [결과 출력]
print("?" if check.count(max(check)) > 1 else chr(check.index(max(check))+97).upper())
