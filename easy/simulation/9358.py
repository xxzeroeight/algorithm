"""
정수로 이루어진 수열이 주어지면, 주어진 규칙에 따라 수열을 접는다.

예제 1:
입력:
2
5
2 5 10 3 -4
3
5 4 -3
출력:
Case #1: Alice
Case #2: Bob

제약 조건:
1 ≤ T ≤ 100
2 ≤ N ≤ 100

풀이:
1. 상근이와 창영이, 둘의 점수를 비교하기 위해 수열의 크기가 2일 때까지 반복한다.
2. 규칙은 아래와 같다.
 2-1. 수열의 첫 번째(i)와 N번째(-1-i)을 더하고, 두 번째 수와 N-1번째 수를 더하는 식이다.
 2-2. 홀수인 경우 같은 수를 두 번 더한다.
"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

# [핵심 로직]
idx = 0
for _ in range(t):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    while len(li) > 2:
        li = [li[i] + li[-1-i] for i in range((len(li)//2)+1)]

    idx += 1

# [결과 출력]
    if li[0] > li[1]: print(f"Case #{idx}: Alice")
    else: print(f"Case #{idx}: Bob")
