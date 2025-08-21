"""
균등한 우주의 쌍의 개수를 조건을 맞게 구한다.

예제 1:
입력:
2 3
1 3 2
12 50 31
출력:
1

예제 2:
입력:
2 3
1 3 2
12 50 10
출력:
0

예제 3:
입력:
5 3
20 10 30
10 20 60
80 25 79
30 50 80
80 25 81
출력:
2

제약 조건:
2 ≤ M ≤ 10
3 ≤ N ≤ 100
1 ≤ 행성의 크기 ≤ 10,000
"""

import sys

# [입력 처리]
m, n = map(int, sys.stdin.readline().split())

li = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# [핵심 로직]
cnt = 0
idx = []
for i in range(m):
    s = sorted(li[i])

    idx.append([li[i].index(s[j])+1 for j in range(n)])

for k in range(m-1):
    for p in range(k+1, m):
        if idx[k] == idx[p]:
            cnt += 1

# [결과 출력]
print(cnt)
