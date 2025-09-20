"""
문제: 카드 놓기
유형: 브루트포스/집합과 맵
난이도: S

시간복잡도: O(P(n, k) x L)
공간복잡도: O(P(n, k) x L)

아이디어:
1. 순열을 이용하여 모든 정수를 만든다.

주의할 점/예외 케이스:

"""

import sys
from itertools import permutations

# [입력 처리]
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

nums = [sys.stdin.readline().rstrip() for _ in range(n)]

# [핵심 로직]
li = list(permutations(nums, k))
ans = {int("".join(map(str, i))) for i in li}

# [결과 출력]
print(len(ans))
