"""
알파벳으로 이루어진 단어들이 주어지면, 조건에 따라 정렬한다.

예제 1:
입력:
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
출력:
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate

제약 조건:
1 ≤ N ≤ 20,000

풀이:
1. 중복을 제거하고 다중 조건 정렬한다. (set+정렬len())
"""

import sys

# [입력 처리]
n = int(sys.stdin.readline())
li = list(set([sys.stdin.readline().rstrip() for _ in range(n)]))

# [핵심 로직]
ans = sorted(li, key=lambda x: (len(x), x))

# [결과 출력]
print(*ans, sep="\n")
