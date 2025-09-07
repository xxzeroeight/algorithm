"""
문자열(이름, 출퇴근 여부)가 주어졌을 때, 현재 회사에 남아있는 사람을 확인한다.

예제 1:
입력:
4
Baha enter
Askar enter
Baha leave
Artem enter
출력:
Askar
Artem

제약 조건:
2 ≤ n ≤ 10^6

풀이:
1. 해시를 이용하여 출퇴근 여부에 따라 추가, 삭제 여부를 정한다.
2. 키(이름)을 기준으로 내림차순 정렬한다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

# [핵심 로직]
table = dict()
for _ in range(n):
    a, b = sys.stdin.readline().split()

    if b == "enter":
        table[a] = b
    else:
        del table[a]

table = sorted(table.keys(), reverse=True)

# [결과 출력]
for key in table:
    print(key)
