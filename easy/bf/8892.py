"""
단어들이 주어지면, 단어들을 합쳐 팰린드롬을 만들 수 있는지 판단한다.

예제 1:
입력:
2
5
aaba
ba
ababa
bbaa
baaba
3
abc
bcd
cde
출력:
abababa
0

제약 조건:
1 ≤ k ≤ 100

풀이:
1. 두 단어를 만들 때 자기 자신을 제외하고 모든 단어와 합쳐져야 한다.
2. 만든 팰린드롬 중 하나를 출력한다. (없으면 0)
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())

    li = [sys.stdin.readline().rstrip() for _ in range(k)]

# [핵심 로직]
    found, result = False, ""
    for i in range(k):
        if found: break

        for j in range(k):
            if i == j:
                continue

            tmp = li[i] + li[j]
            if tmp == tmp[::-1]:
                result = tmp
                found = True
                break

# [결과 출력]
    print(result if found else 0)
