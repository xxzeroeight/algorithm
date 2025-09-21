"""
문제: 최대 GCD
유형: 브루트포스/수학
난이도: S

시간복잡도: O(n x k^2 x log(max_value))
공간복잡도: O(n x k)

아이디어:
1. 두 수의 쌍 중에서 가장 큰 최대공약수를 찾는다.

주의할 점/예외 케이스:

"""

import math
import sys

# [입력 처리]
n = int(sys.stdin.readline())

li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# [핵심 로직]
for l in li:
    ans = 0

    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            ans = max(ans, math.gcd(l[i], l[j]))

# [결과 출력]
    print(ans)
