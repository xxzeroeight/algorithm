"""
두 문자열(삭제 전, 후)이 주어지면, n번 덮어썼을 때 문자열끼리 일치하는지 확인한다.

예제 1:
입력:
1
10001110101000001111010100001110
01110001010111110000101011110001
출력: Deletion succeeded

예제 2:
입력:
20
0001100011001010
0001000011000100
출력: Deletion failed

제약 조건:
N(1 ≤ N ≤ 20)
비트는 최대 1000개의 문자로 이루어져 있다.
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

before = sys.stdin.readline().rstrip()
after = sys.stdin.readline().rstrip()

# [핵심 로직]
if n % 2 != 0:
    flag = True
    for i in range(len(before)):
        if before[i] == after[i]:
            flag = False
            break

    print("Deletion succeeded" if flag else "Deletion failed")
else:
    print("Deletion succeeded" if before == after else "Deletion failed")

# [결과 출력]

