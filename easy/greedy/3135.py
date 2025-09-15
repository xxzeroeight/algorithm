"""
문제: 라디오
유형: 그리디/수학
난이도: S

시간복잡도: O(n)
공간복잡도: O(n)

아이디어:
1. (미리 지정되어 있는 주파수 - 듣고 싶은 주파수)와 (현재 주파수 - 듣고 싶은 주파수)중 더 작은 값은 구한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
a, b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

li = [abs(int(sys.stdin.readline())-b) for _ in range(n)]

# [핵심 로직]
mv = min(abs(a-b), min(li))

# [결과 출력]
print(abs(a-b) if mv == abs((a-b)) else mv+1)
