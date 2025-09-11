"""
소의 위치를 셔플한 후의 최종 순서가 주어졌을 때, 초기 순서를 구한다.

예제 1:
입력:
5
1 3 4 5 2
1234567 2222222 3333333 4444444 5555555
출력:
1234567
5555555
2222222
3333333
4444444

제약 조건:
1 ≤ N ≤ 100

풀이:
1. 3번 셔플된 순서가 입력으로 주어졌기 때문에, 3번 더 셔플하면 초기상태를 알 수 있다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]
for _ in range(3):
    c = [c[s[i]-1] for i in range(n)]

# [결과 출력]
print(*c, sep="\n")
