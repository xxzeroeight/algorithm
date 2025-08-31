"""
요리시간이 주어지면, 전자레인지의 시간버튼을 눌러 정확히 요리시간과 일치시킨다.

예제 1:
입력: 100
출력: 0 1 4

예제 2:
입력: 189
출력: -1

제약 조건:
1 ≤ T ≤ 10,000
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

# [핵심 로직]
time = [300, 60, 10]
ans = [0, 0, 0]

for i in range(3):
    ans[i] = t // time[i]
    t %= time[i]

# [결과 출력]
if t == 0:
    print(*ans)
else:
    print(-1)
