"""
문제: 부분 문자열
유형: 그리디/문자열
난이도: S

시간복잡도: O(k x m)
공간복잡도: O(n + m)

아이디어:
1. t문자열을 순회하면서 s문자열이 완성되는지 확인한다.

주의할 점/예외 케이스:

"""

import sys

# [입력 처리]
while 1:
    try:
        s, t = sys.stdin.readline().split()

# [핵심 로직]
        idx, flag = 0, False
        for i in range(len(t)):
            if s[idx] == t[i]:
                idx += 1

            if idx == len(s):
                flag = True
                break

# [결과 출력]
        print("Yes" if flag else "No")

    except:
        break