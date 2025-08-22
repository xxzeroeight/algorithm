"""
5x7크기의 그림들이 주어졌을 때, 가장 비슷(다른 칸의 개수가 가장 적은)한 그림을 찾는다.

예제 1:
입력:
3
..X....
.XXX...
.XX....
.....X.
.X...X.
...X...
..XX...
.XX....
.XX..X.
.X...X.
XX.....
X......
XX...XX
XXXX.XX
XXX..XX
출력:
1 2
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

li = [[list(sys.stdin.readline().rstrip()) for _ in range(5)] for _ in range(n)]

# [핵심 로직]
mv = sys.maxsize
r1, r2 = 0, 0
for i in range(n-1):
    for j in range(i+1, n):

        cnt = 0
        for k in range(5):
            for p in range(7):
                if li[i][k][p] != li[j][k][p]:
                    cnt += 1

        if mv > cnt:
            mv = cnt
            r1 = i+1
            r2 = j+1

# [결과 출력]
print(r1, r2)
