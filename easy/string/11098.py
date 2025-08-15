"""
선수의 몸값과 선수 이름이 주어지면, 그 중 가장 비싼 몸값의 선수를 찾는다.

예제 1:
입력:
2
3
10 Iversen
1000000 Nannskog
2000000 Ronaldinho
2
1000000 Maradona
999999 Batistuta
출력:
Ronaldinho
Maradona

제약 조건:
n≤100
1≤p≤100
C<2*10^9
선수의 이름은 20자 이하여야 하며, 사이에 공백이 있어서는 안 된다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

for _ in range(n):
    p = int(sys.stdin.readline().rstrip())

    li = [[int(price), name] for price, name in [sys.stdin.readline().split() for _ in range(p)]]

# [핵심 로직]
    res = sorted(li, key=lambda x:x[0], reverse=True)

# [결과 출력]
    print(res[0][1])
