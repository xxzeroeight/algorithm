"""


예제 1:
입력:
출력:


제약 조건:


풀이:

"""

import sys

# [입력 처리]
t = int(sys.stdin.readline())

# [핵심 로직]
cnt = 0
for _ in range(t):
    num = sys.stdin.readline().rstrip()

    while num != "6174":
        n = int("".join(sorted(list(num), reverse=True))) - int("".join(sorted(list(num))))

        cnt += 1

        num = "".join(sorted(list(str(n)), reverse=True))

# [결과 출력]
    print(cnt)

# 2025-09-09, 시도: 2