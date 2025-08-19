"""
문자열(시험의 정답)이 주어지면, 패턴과 비교한다.
최댓값과 사람을 출력한다.

예제 1:
입력:
5
BAACC
출력:
3
Bruno

예제 2:
입력:
9
AAAABBBBB
출력:
4
Adrian
Bruno
Goran

제약 조건:
1 ≤ N ≤ 100
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())
p = list(sys.stdin.readline().rstrip())

# [핵심 로직]
s = ["A", "B", "C"] * (n//3) + ["A", "B", "C"][:n%3]
c = ["B", "A", "B", "C"] * (n//4) + ["B", "A", "B", "C"][:n%4]
h = ["C", "C", "A", "A", "B", "B"] * (n//6) + ["C", "C", "A", "A", "B", "B"][:n%6]

ss, cc, hh = 0, 0, 0
for i in range(n):
    if p[i] == s[i]: ss += 1
    if p[i] == c[i]: cc += 1
    if p[i] == h[i]: hh += 1

# [결과 출력]
print(max(ss, cc, hh))
if max(ss, cc, hh) == ss: print("Adrian")
if max(ss, cc, hh) == cc: print("Bruno")
if max(ss, cc, hh) == hh: print("Goran")
