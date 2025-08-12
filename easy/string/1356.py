"""
정수가 주어지면, 유진수인지 판단한다.
유진수: 어떤 수를 10진수로 표현한 뒤 그 수를 두 부분으로 나눴을 때, 앞부분 자리수의 곱과 뒷부분 자리수의 곱이 같을 때

예제 1:
입력: 1236
출력: YES

예제 2:
입력: 1
출력: NO

예제 3:
입력: 1221
출력: YES

예제 4:
입력: 4729382
출력: NO

예제 5:
입력: 42393338
출력: YES

제약 조건:
수는 2,147,483,647보다 작거나 같은 자연수이다.
"""

import sys

def multiple(li):
    s = 1
    for l in li:
        s *= int(l)

    return s

# [입력 처리]
n = sys.stdin.readline().rstrip()

# [핵심 로직]
for i in range(1, len(n)):
    if multiple(n[:i]) == multiple(n[i:]):
        print("YES")
        break
else:
    print("NO")

# [결과 출력]

