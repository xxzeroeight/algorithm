"""
문자열에서 ":-)"과 ":-("을 찾는다.

예제 1:
입력: How are you :-) doing :-( today :-)?
출력: happy

예제 2:
입력: :)
출력: none

예제 3:
입력: This:-(is str:-(:-(ange te:-)xt.
출력: sad

제약 조건:
최소 1개에서 최대 255개의 문자들이 입력된다.
"""

import sys

# [입력 처리]
m = sys.stdin.readline().rstrip()

# [핵심 로직]
h = m.count(":-)")
s = m.count(":-(")

# [결과 출력]
print("happy" if h > s else "none" if h == 0 and s == 0 else "sad" if h < s else "unsure")
