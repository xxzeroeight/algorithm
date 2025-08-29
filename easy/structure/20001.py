"""
주어지는 문자열에 따라 문제를 추가할 것인지 뺄 것인지 정한다.

예제 1:
입력:
고무오리 디버깅 시작
문제
고무오리
문제
문제
고무오리
고무오리
고무오리 디버깅 끝
출력:
고무오리야 사랑해

예제 2:
입력:
고무오리 디버깅 시작
고무오리
고무오리
고무오리
고무오리 디버깅 끝
출력:
고무오리야 사랑해

예제 3:
입력:
고무오리 디버깅 시작
문제
문제
고무오리
고무오리
고무오리
문제
고무오리
문제
고무오리
고무오리
고무오리
고무오리 디버깅 끝
출력:
고무오리야 사랑해

예제 4:
입력:
고무오리 디버깅 시작
고무오리
고무오리 디버깅 끝
출력:
힝구
"""

import sys

# [입력 처리]
start = sys.stdin.readline().rstrip()

stack = []
while 1:
    s = sys.stdin.readline().rstrip()

# [핵심 로직]
    if s == "고무오리 디버깅 끝":
        break

    if s == "고무오리":
        if not stack:
            stack.append("문제")
            stack.append("문제")
        else:
            stack.pop()
    else:
        stack.append("문제")

# [결과 출력]
print("고무오리야 사랑해" if not stack else "힝구")
