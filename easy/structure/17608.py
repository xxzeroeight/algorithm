"""
막대기를 오른쪽에서 봤을 때, 몇 개가 보이는지 센다.

예제 1:
입력:
6
6
9
7
6
4
6
출력:
3

예제 2:
입력:
5
5
4
3
2
1
출력:
5

제약 조건:
2 ≤ N ≤ 100,000
1 ≤ h ≤ 100,000
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())

li = [int(sys.stdin.readline()) for _ in range(n)][::-1]

# [핵심 로직]
cnt, stack = 1, [li[0]]
for l in li[1:]:
    if stack[-1] < l:
        stack.append(l)

# [결과 출력]
print(len(stack))
