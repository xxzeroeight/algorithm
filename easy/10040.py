"""
경기와 위원의 수가 주어진다.
경기를 개최하는데 필요한 비용이 심사 기준 이하인 경기 중에서 가장 재미있는 경기를 고른다.

예제 1:
입력:
4 3
5
3
1
4
4
3
2
출력:
2

제약 조건:
1 ≤ N, M ≤ 1000
1 ≤ A_i ≤ 1000
1 ≤ B_j ≤ 1000
"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())

game = [int(sys.stdin.readline()) for _ in range(n)]

cnt = [0] * n
for _ in range(m):
    v = int(sys.stdin.readline())

# [핵심 로직]
    for i in range(len(game)):
        if game[i] <= v:
            cnt[i] += 1
            break

# [결과 출력]
print(cnt.index(max(cnt))+1)
