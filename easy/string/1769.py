"""
X가 주어졌을 때, 변환 과정의 횟수와 3의 배수인지 구한다.

예제 1:
입력:
1234567
출력:
3
NO

제약 조건:
X는 1,000,000자리 이하의 수이다.

풀이:
1. X가 한자리 수가 될 때까지 각 자리수의 합을 더한다.
2. 한자리 수가 될 때까지의 횟수와 이 수가 3의 배수인지 판단한다.
"""

import sys

# [입력 처리]
x = sys.stdin.readline().rstrip()

# [핵심 로직]
cnt = 0
while 1:
    if len(x) == 1:
        break

    s = 0
    for w in x:
        s += int(w)

    x = str(s)
    cnt += 1

# [결과 출력]
print(cnt)
print("YES" if int(x) % 3 == 0 else "NO")
