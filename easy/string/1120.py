"""
문제: 문자열
유형: 문자열/브루트포스
난이도: S

시간복잡도: O(mn)
공간복잡도: O(m - n + 1)

아이디어:
1. 문자열 b에서 len(a)인 모든 부분 문자열을 검사한다.
2. 각 부분 문자열과 a사이의 일치하는 문자 개수를 센다.
3. 가장 많이 일치하는 경우를 찾아서, 변경해야 할 문자 개수를 출력한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
a, b = sys.stdin.readline().split()

# [핵심 로직]
ans = []
for i in range(len(b)-len(a)+1):
    tmp = b[i:i+len(a)]

    cnt = 0
    for j in range(len(a)):
        if a[j] == tmp[j]:
            cnt += 1

    ans.append(cnt)

# [결과 출력]
print(len(a) - max(ans))
