"""
재환이가 낼 수 있는 "aah"가 주어지고, 자기가 소리낼 수 있는 길이의 "aah"를 요구하는 의사를 만난다.
모든 의사는 자신이 원하는 길이의 "aah"를 들어야 한다.

예제 1:
입력:
aaah
aaaaah
출력:
no

예제 2:
입력:
aaah
ah
출력:
go

제약 조건:
a의 개수는 0보다 크거나 같고, 999보다 작거나 같으며, 항상 h는 마지막에 하나만 주어진다.
"""

import sys

# [입력 처리]
j = sys.stdin.readline().rstrip()
d = sys.stdin.readline().rstrip()

# [핵심 로직]


# [결과 출력]
print("no" if len(j) < len(d) else "go")
