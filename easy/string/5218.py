"""
길이가 같은 두 단어가 주어졌을 때, 각 단어에 포함된 모든 글자의 거리를 구한다.

예제 1:
입력:
5
AAAA ABCD
ABCD AAAA
DARK LOKI
STRONG THANOS
DEADLY ULTIMO
출력:
Distances: 0 1 2 3
Distances: 0 25 24 23
Distances: 8 14 19 24
Distances: 1 14 9 25 1 12
Distances: 17 7 19 5 1 16

제약 조건:
테스트 케이스의 수 (< 100)
단어의 길이는 4보다 크거나 같고, 20보다 작거나 같으며, 알파벳 대문자로만 이루어져 있다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    x, y = sys.stdin.readline().split()

# [핵심 로직]
    li = []
    for i in range(len(x)):
        if x[i] > y[i]:
            li.append(ord(y[i]) + 26 - ord(x[i]))
        else:
            li.append(ord(y[i]) - ord(x[i]))

# [결과 출력]
    print(f"Distances: {" ".join(map(str, li))}")
