"""
투표 결과가 주어졌을 때, 누가 표를 더 많이 받았는지 출력한다.

예제 1:
입력:
6
ABBABB
출력: B

제약 조건:
심사위원의 수 V (1 ≤  V ≤  15)
"""

import sys

# [입력 처리]
v = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

# [핵심 로직]


# [결과 출력]
print("A" if s.count("A") > s.count("B") else "B" if s.count("A") < s.count("B") else "Tie")
