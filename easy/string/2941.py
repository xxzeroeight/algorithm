"""
문자열이 주어지면, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다. (목록에 없는 글자도 한 글자로 센다.)

예제 1:
입력: ljes=njak
출력: 6

예제 2:
입력: ddz=z=
출력: 3

예제 3:
입력: nljj
출력: 3

예제 4:
입력: c=c=
출력: 2

예제 5:
입력: dz=ak
출력: 3

풀이:
1. 변경된 형태(table)에 해당하는 알파벳을 "*"로 변환한다.
2. "*"로 변환된 알파벳의 수 + 목록에 없는 알파벳의 수
"""

import sys

# [입력 처리]
s = sys.stdin.readline().rstrip()

# [핵심 로직]
table = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for idx in table:
    s = s.replace(idx, "*")

# [결과 출력]
print(len(s))
