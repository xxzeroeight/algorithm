"""
N개의 빈 박스에 M개의 책을 넣는다.
이때 책의 크기가 박스의 크기를 넘지 않도록 한다.
위 방법대로 넣었을 때 낭비된 박스의 합을 구한다.

예제 1:
입력:
3 3
5 5 5
5 5 5
출력:
0

예제 2:
입력:
3 1
2 3 5
3
출력:
3

예제 3:
입력:
3 1
2 3 5
3
출력:
7

예제 4:
입력:
4 5
3 4 5 6
3 3 3 3 3
출력:
3

제약 조건:
1 ≤ N, M ≤ 50
1 ≤ A_i, B_j ≤ 1,000
"""

import sys

# [입력 처리]
n, m = map(int, sys.stdin.readline().split())

box = list(map(int, sys.stdin.readline().split()))
books = list(map(int, sys.stdin.readline().split()))

# [핵심 로직]


# [결과 출력]
print(sum(box) - sum(books))
