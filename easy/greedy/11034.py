"""
캥거루의 위치가 주어지면, 다른 두 위치 사이에서 최대 몇 번 움직(간격이 큰)일 수 있는지 센다.

예제 1:
입력:
2 3 5
3 5 9
출력:
1
3

제약 조건:
0 < A < B < C < 100
"""

import sys

# [입력 처리]
while 1:
    try:
        a, b, c = map(int, sys.stdin.readline().split())

# [핵심 로직]
        ans = max((b-a), (c-b)) - 1

        print(ans)

# [결과 출력]
    except:
        break
