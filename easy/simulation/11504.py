"""
정수로 되어있는 돌림판에서 X와 Y사이에 값들이 몇 개인지 센다.

예제 1:
입력:
3
8 3
2 0 0
3 1 1
3 7 8 3 1 9 2 7
5 2
8 8
9 9
1 3 2 5 4
6 3
0 0 0
9 9 9
1 2 3 4 5 6
출력:
1
0
6

제약 조건:
1 ≤ N ≤ 100
1 ≤ M ≤ 9, M ≤ N

풀이:
1. 돌림판에서 X와 Y의 자릿수만큼 숫자를 뽑는다.
2. X <= 찾은 수 <= Y 조건에 맞는 숫자의 개수를 센다. (중복 가능)
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

# [핵심 로직]
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    x = int("".join(list(sys.stdin.readline().split())))
    y = int("".join(list(sys.stdin.readline().split())))
    li = list(sys.stdin.readline().split())

    wheel = li + li[:m-1]

    cnt = 0
    for i in range(len(wheel)-m+1):
        if x <= int("".join(wheel[i:i+m])) <= y:
            cnt += 1

# [결과 출력]
    print(cnt)
