"""
두 정수 n, m 사이에 있는 숫자 중 반복되는 숫자가 없도록 방 번호를 만든다.

예제 1:
입력:
87 104
989 1022
22 25
1234 1234
출력:
14
0
3
1

제약 조건:
1 ≤ N ≤ M ≤ 5000

풀이:
1. n~m사이의 숫자 중 반복되지 않는 숫자를 센다. (set())
"""

import sys

# [입력 처리]
while 1:
    try:
        n, m = map(int, sys.stdin.readline().split())

# [핵심 로직]
        cnt = 0
        for i in range(n, m+1):
            if len(set(str(i))) == len(str(i)):
                cnt += 1

        print(cnt)

# [결과 출력]
    except:
        break
