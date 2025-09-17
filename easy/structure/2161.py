"""
문제: 카드1
유형: 자료구조
난이도: S

시간복잡도: O(n)
공간복잡도: O(n)

아이디어:
1. deque를 사용하여 맨 앞 숫자를 빼고, 그 다음 숫자르 맨 뒤에 삽입시키는 과정을 반복한다.

주의할 점/예외 케이스:

"""

import sys
from collections import deque

# [입력 처리]
n = int(sys.stdin.readline())

# [핵심 로직]
dq = deque(range(1, n+1))

ans = []
for i in range(n-1):
    ans.append(dq.popleft())
    dq.append(dq.popleft())

# [결과 출력]
print(*ans, *dq)
