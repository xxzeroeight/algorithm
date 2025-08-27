"""
입력으로 주어지는 수가 한 자리가 될 때까지 반복한 횟수를 센다.

예제 1:
입력: 5
출력: 0

예제 2:
입력: 10
출력: 1

예제 3:
입력: 679
출력: 5
"""

import sys

# [입력 처리]
t = sys.stdin.readline().rstrip()

# [핵심 로직]
cnt = 0
while len(t) > 1:
    s = 1
    for w in t:
        s *= int(w)

    cnt += 1
    t = str(s)

# [결과 출력]
print(cnt)
