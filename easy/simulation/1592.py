"""
다른 사람에게 정해진 규칙에 따라 공을 던진다.
공을 받은 횟수가 홀수번이면 시계 방향으로 L번째, 공을 받은 횟수가 짝수번이면 반시계 방향으로 L번째
M번 던지는 사람이 나타날 때에 공을 총 몇 번 던졌는지 센다.

예제 1:
입력: 5 3 2
출력: 10

예제 2:
입력: 4 1 3
출력: 0

예제 3:
입력: 10 3 5
출력: 4

예제 4:
입력: 15 4 9
출력: 15

제약 조건:
N은 3보다 크거나 같고, 50보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다. L은 N-1보다 작거나 같은 자연수이다.
"""

import sys

# [입력 처리]
n, m, l = map(int, sys.stdin.readline().split())

# [핵심 로직]
check = 0
balls = [0] * n

cnt = 0
while 1:
    check = (check+l)%n if balls[check] % 2 == 0 else (check-l)%n
    balls[check] += 1

    if max(balls) == m:
        break

    cnt += 1

# [결과 출력]
print(cnt)
