"""
봉우리 높이가 주어졌을 때, 자신보다 작은 값들의 개수의 최댓값을 구한다.

예제 1:
입력:
7
6 4 10 2 5 7 11
출력:
3

제약 조건:
1 ≤ N ≤ 30,000
1 ≤ 높이 ≤ 100,000
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
cnt, mv, ans = 0, 0, 0
for l in li:
    if mv < l:
        mv = l
        cnt = 0
    else:
        cnt += 1

    ans = max(ans, cnt)

# [결과 출력]
print(ans)
