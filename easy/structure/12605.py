"""
문자열이 주어지면, 단어들의 순서를 반대로 출력한다.

예제 1:
입력:
3
this is a test
foobar
all your base
출력:
Case #1: test a is this
Case #2: foobar
Case #3: base your all

제약 조건:
1 ≤ L ≤ 25
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

for i in range(n):
    li = list(sys.stdin.readline().split())

# [핵심 로직]
    stack = []
    for _ in range(len(li)):
        stack.append(li.pop())

# [결과 출력]
    print(f"Case #{i+1}:", *stack)
