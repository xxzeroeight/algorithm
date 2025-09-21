"""
문제: 한수
유형: 브루트포스/수학
난이도: S

시간복잡도: O(x)
공간복잡도: O(1)

아이디어:
1. 등차수열인지 판별하기 위한 조건
 1-1. 2자리 숫자의 경우: 모든 수가 한수
 1-2. 3자리 숫자의 경우: 두 번째 자릿수 - 첫 번째 자릿수 == 세 번째 자릿수 - 두 번째 자릿수

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
x = int(sys.stdin.readline())

# [핵심 로직]
if x < 100: print(x)
else:
    cnt = 99

    for i in range(100, x+1):
        n = [int(d) for d in str(i)]

        if n[1] - n[0] == n[2] - n[1]:
            cnt += 1

# [결과 출력]
    print(cnt)
